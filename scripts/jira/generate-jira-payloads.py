#!/usr/bin/env python3
"""Generate offline Jira payload JSON from AI SDLC artifacts.

This script intentionally does not call Jira APIs.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = SCRIPT_DIR / "templates"
REPO_ROOT = SCRIPT_DIR.parents[1]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def clean(value: str | None) -> str:
    if value is None:
        return ""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        value = value[1:-1]
    if len(value) >= 2 and value[0] == value[-1] == "`":
        value = value[1:-1]
    return value.strip()


def parse_workflow_state(path: Path) -> dict[str, dict[str, str]]:
    sections: dict[str, dict[str, str]] = {}
    current_section = ""

    for raw_line in read_text(path).splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("- "):
            continue

        if not raw_line.startswith(" ") and raw_line.endswith(":"):
            current_section = raw_line[:-1].strip()
            sections.setdefault(current_section, {})
            continue

        if current_section and raw_line.startswith("  "):
            match = re.match(r"\s{2}([A-Za-z0-9_]+):\s*(.*)$", raw_line)
            if match:
                sections[current_section][match.group(1)] = clean(match.group(2))

    return sections


def parse_metadata(markdown: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    match = re.search(r"^## Metadata\s*\n(?P<body>.*?)(?:\n## |\Z)", markdown, flags=re.M | re.S)
    if not match:
        return metadata

    for row in parse_markdown_table(match.group("body")):
        field = row.get("Field", "")
        value = row.get("Value", "")
        if field:
            metadata[field] = clean(value)
    return metadata


def section(markdown: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*\n(?P<body>.*?)(?:\n## |\Z)"
    match = re.search(pattern, markdown, flags=re.M | re.S)
    return match.group("body").strip() if match else ""


def first_paragraph(markdown: str, heading: str) -> str:
    body = section(markdown, heading)
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", body) if part.strip()]
    return paragraphs[0] if paragraphs else ""


def parse_markdown_table(markdown: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    lines = [line.rstrip() for line in markdown.splitlines() if line.strip().startswith("|")]

    index = 0
    while index + 1 < len(lines):
        header = split_table_row(lines[index])
        separator = split_table_row(lines[index + 1])
        if not header or not all(re.fullmatch(r":?-{2,}:?", cell.strip()) for cell in separator):
            index += 1
            continue

        index += 2
        while index < len(lines):
            cells = split_table_row(lines[index])
            if len(cells) != len(header):
                break
            rows.append({header[column]: clean(cells[column]) for column in range(len(header))})
            index += 1
        continue

    return rows


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def rows_in_section(markdown: str, heading: str) -> list[dict[str, str]]:
    return parse_markdown_table(section(markdown, heading))


def load_template(name: str) -> dict[str, Any]:
    return json.loads(read_text(TEMPLATE_DIR / f"{name}.json"))


def render(value: Any, context: dict[str, str]) -> Any:
    if isinstance(value, str):
        rendered = value
        for key, replacement in context.items():
            rendered = rendered.replace("{{" + key + "}}", replacement)
        return rendered
    if isinstance(value, list):
        return [render(item, context) for item in value]
    if isinstance(value, dict):
        return {key: render(item, context) for key, item in value.items()}
    return value


def relative_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def slug(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9]+", "-", value.strip()).strip("-").lower()
    return value or "item"


def artifact_path(raw_path: str) -> Path | None:
    raw_path = clean(raw_path)
    if not raw_path:
        return None
    path = Path(raw_path)
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path


def base_context(workflow_path: Path, workflow: dict[str, dict[str, str]], intent_metadata: dict[str, str]) -> dict[str, str]:
    capability = workflow.get("capability", {})
    workflow_values = workflow.get("workflow", {})
    return {
        "domain": capability.get("domain", intent_metadata.get("Domain", "")),
        "capability": capability.get("name", intent_metadata.get("Capability", "")),
        "capability_id": capability.get("capability_id", slug(intent_metadata.get("Capability", "capability"))),
        "workflow_state": workflow_values.get("current_state", ""),
        "workflow_skill": workflow_values.get("current_skill", ""),
        "confluence_page": capability.get("confluence_page", intent_metadata.get("Confluence Page", "")),
        "source_artifact": relative_path(workflow_path),
    }


def build_epic(workflow_path: Path, workflow: dict[str, dict[str, str]], intent_markdown: str) -> dict[str, Any]:
    intent_metadata = parse_metadata(intent_markdown)
    context = base_context(workflow_path, workflow, intent_metadata)
    epic_key = workflow.get("capability", {}).get("jira_epic") or intent_metadata.get("Jira Epic")
    context.update(
        {
            "external_id": epic_key or f"EPIC-{context['capability_id'].upper()}",
            "summary": context["capability"],
            "description": "\n\n".join(
                part
                for part in [
                    first_paragraph(intent_markdown, "Problem Statement"),
                    first_paragraph(intent_markdown, "Desired Outcomes"),
                ]
                if part
            ),
            "source_artifact": relative_path(workflow_path),
        }
    )
    return render(load_template("epic"), context)


def build_stories(workflow_path: Path, workflow: dict[str, dict[str, str]], spec_path: Path, spec_markdown: str, intent_metadata: dict[str, str]) -> list[dict[str, Any]]:
    context = base_context(workflow_path, workflow, intent_metadata)
    epic_key = workflow.get("capability", {}).get("jira_epic") or intent_metadata.get("Jira Epic", "")
    stories: list[dict[str, Any]] = []

    requirement_rows = rows_in_section(spec_markdown, "Functional Requirements")
    requirement_rows.extend(rows_in_section(spec_markdown, "Non-Functional Requirements"))

    for index, row in enumerate(requirement_rows, start=1):
        req_id = row.get("Req ID") or row.get("NFR ID") or row.get("Requirement ID") or f"REQ-{index:03d}"
        requirement = row.get("Requirement", "")
        jira = row.get("Jira", "")
        context_for_row = {
            **context,
            "external_id": jira or req_id,
            "parent_external_id": epic_key,
            "summary": f"{req_id} {requirement}".strip(),
            "description": requirement,
            "priority": row.get("Priority", ""),
            "acceptance_criteria": row.get("Acceptance Criteria", row.get("Acceptance", "")),
            "source_artifact": relative_path(spec_path),
        }
        stories.append(render(load_template("story"), context_for_row))

    return stories


def build_tasks(workflow_path: Path, workflow: dict[str, dict[str, str]], plan_path: Path, plan_markdown: str, intent_metadata: dict[str, str]) -> list[dict[str, Any]]:
    context = base_context(workflow_path, workflow, intent_metadata)
    epic_key = workflow.get("capability", {}).get("jira_epic") or intent_metadata.get("Jira Epic", "")
    tasks: list[dict[str, Any]] = []

    for index, row in enumerate(rows_in_section(plan_markdown, "Proposed Implementation Slices"), start=1):
        slice_name = row.get("Slice", f"Slice {index}")
        jira = row.get("Jira Placeholder", "")
        context_for_row = {
            **context,
            "external_id": jira or f"TASK-{context['capability_id'].upper()}-{index:03d}",
            "parent_external_id": epic_key,
            "summary": slice_name,
            "description": row.get("Scope", ""),
            "requirement_coverage": row.get("Requirement Coverage", ""),
            "acceptance_coverage": row.get("Acceptance Coverage", ""),
            "code_readiness": row.get("Code Readiness", ""),
            "source_artifact": relative_path(plan_path),
        }
        tasks.append(render(load_template("task"), context_for_row))

    return tasks


def build_defects(workflow_path: Path, workflow: dict[str, dict[str, str]], validation_path: Path, validation_markdown: str, intent_metadata: dict[str, str]) -> list[dict[str, Any]]:
    context = base_context(workflow_path, workflow, intent_metadata)
    epic_key = workflow.get("capability", {}).get("jira_epic") or intent_metadata.get("Jira Epic", "")
    validation_metadata = parse_metadata(validation_markdown)
    validation_status = validation_metadata.get("Validation Status", "")
    findings = section(validation_markdown, "Defects Or Gaps")
    defects: list[dict[str, Any]] = []

    if re.search(r"\bNo validation defects\b", findings, flags=re.I):
        return defects

    bullet_lines = [line.strip("- ").strip() for line in findings.splitlines() if line.strip().startswith("- ")]

    for index, finding in enumerate(bullet_lines, start=1):
        context_for_row = {
            **context,
            "external_id": f"DEFECT-{context['capability_id'].upper()}-{index:03d}",
            "parent_external_id": epic_key,
            "summary": finding,
            "description": finding,
            "validation_status": validation_status,
            "source_artifact": relative_path(validation_path),
        }
        defects.append(render(load_template("defect"), context_for_row))

    return defects


def build_decisions(workflow_path: Path, workflow: dict[str, dict[str, str]], intent_metadata: dict[str, str]) -> list[dict[str, Any]]:
    context = base_context(workflow_path, workflow, intent_metadata)
    epic_key = workflow.get("capability", {}).get("jira_epic") or intent_metadata.get("Jira Epic", "")
    decisions: list[dict[str, Any]] = []
    jira_epic = workflow.get("capability", {}).get("jira_epic", "")
    jira_prefix = "-".join(jira_epic.split("-")[:2]) if jira_epic else ""
    capability_needles = [
        context["capability"].lower(),
        context["capability_id"].lower(),
        jira_prefix.lower(),
    ]

    for adr_path in sorted((REPO_ROOT / "decisions").glob("ADR-*.md")):
        markdown = read_text(adr_path)
        title_match = re.search(r"^#\s+(.+)$", markdown, flags=re.M)
        status_match = re.search(r"^## Status\s*\n(?P<status>.*?)(?:\n## |\Z)", markdown, flags=re.M | re.S)
        title = clean(title_match.group(1)) if title_match else adr_path.stem
        searchable = f"{adr_path.stem}\n{title}\n{markdown}".lower()
        if not any(needle and needle in searchable for needle in capability_needles):
            continue
        decision_status = clean(status_match.group("status").splitlines()[0]) if status_match else ""
        context_for_row = {
            **context,
            "external_id": adr_path.stem,
            "parent_external_id": epic_key,
            "summary": title,
            "description": first_paragraph(markdown, "Decision") or first_paragraph(markdown, "Context"),
            "decision_status": decision_status,
            "source_artifact": relative_path(adr_path),
        }
        decisions.append(render(load_template("decision"), context_for_row))

    return decisions


def build_release(workflow_path: Path, workflow: dict[str, dict[str, str]], validation_path: Path, validation_markdown: str, intent_metadata: dict[str, str]) -> dict[str, Any]:
    context = base_context(workflow_path, workflow, intent_metadata)
    epic_key = workflow.get("capability", {}).get("jira_epic") or intent_metadata.get("Jira Epic", "")
    validation_metadata = parse_metadata(validation_markdown)
    release_readiness = first_paragraph(validation_markdown, "Release Readiness")
    validation_id = validation_metadata.get("Validation Report ID", context["capability_id"].upper())
    context.update(
        {
            "external_id": f"RELEASE-{validation_id}",
            "parent_external_id": epic_key,
            "summary": f"{context['capability']} validation and release package",
            "description": "\n\n".join(
                part
                for part in [
                    section(validation_markdown, "Scope Of Validation"),
                    release_readiness,
                ]
                if part
            ),
            "validation_status": validation_metadata.get("Validation Status", ""),
            "release_readiness": release_readiness,
            "source_artifact": relative_path(validation_path),
        }
    )
    return render(load_template("release"), context)


def write_payloads(output_dir: Path, bundle: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "payload-bundle.json").write_text(json.dumps(bundle, indent=2) + "\n", encoding="utf-8")
    (output_dir / "epic.json").write_text(json.dumps(bundle["epic"], indent=2) + "\n", encoding="utf-8")
    (output_dir / "release.json").write_text(json.dumps(bundle["release"], indent=2) + "\n", encoding="utf-8")

    for group_name in ("stories", "tasks", "defects", "decisions"):
        group_dir = output_dir / group_name
        group_dir.mkdir(exist_ok=True)
        for index, payload in enumerate(bundle[group_name], start=1):
            issue_id = slug(payload.get("externalId", f"{group_name}-{index:03d}"))
            (group_dir / f"{issue_id}.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def generate(workflow_state_path: Path) -> dict[str, Any]:
    workflow = parse_workflow_state(workflow_state_path)
    artifacts = workflow.get("artifacts", {})

    intent_path = artifact_path(artifacts.get("intent", ""))
    spec_path = artifact_path(artifacts.get("specification", ""))
    plan_path = artifact_path(artifacts.get("implementation_plan", ""))
    validation_path = artifact_path(artifacts.get("validation_report", ""))

    missing = [
        str(path)
        for path in (intent_path, spec_path, plan_path, validation_path)
        if path is None or not path.exists()
    ]
    if missing:
        raise SystemExit("Missing required artifact(s): " + ", ".join(missing))

    intent_markdown = read_text(intent_path)
    spec_markdown = read_text(spec_path)
    plan_markdown = read_text(plan_path)
    validation_markdown = read_text(validation_path)
    intent_metadata = parse_metadata(intent_markdown)

    return {
        "epic": build_epic(workflow_state_path, workflow, intent_markdown),
        "stories": build_stories(workflow_state_path, workflow, spec_path, spec_markdown, intent_metadata),
        "tasks": build_tasks(workflow_state_path, workflow, plan_path, plan_markdown, intent_metadata),
        "defects": build_defects(workflow_state_path, workflow, validation_path, validation_markdown, intent_metadata),
        "decisions": build_decisions(workflow_state_path, workflow, intent_metadata),
        "release": build_release(workflow_state_path, workflow, validation_path, validation_markdown, intent_metadata),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate offline Jira payload JSON from AI SDLC artifacts.")
    parser.add_argument("--workflow-state", required=True, type=Path, help="Path to workflow-state.yaml.")
    parser.add_argument("--output-dir", type=Path, help="Optional directory for generated payload JSON files.")
    args = parser.parse_args()

    workflow_state_path = args.workflow_state
    if not workflow_state_path.is_absolute():
        workflow_state_path = REPO_ROOT / workflow_state_path
    if not workflow_state_path.exists():
        raise SystemExit(f"Workflow state file not found: {workflow_state_path}")

    bundle = generate(workflow_state_path)

    if args.output_dir:
        write_payloads(args.output_dir, bundle)
        print(f"Wrote Jira payloads to {args.output_dir}")
    else:
        print(json.dumps(bundle, indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
