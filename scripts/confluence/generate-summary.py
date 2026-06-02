#!/usr/bin/env python3
"""Generate offline Confluence summary drafts from AI SDLC Git artifacts.

This script intentionally does not call Confluence APIs.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


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


def relative_path(path: Path | None) -> str:
    if path is None:
        return ""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def resolve_path(raw_path: str) -> Path | None:
    raw_path = clean(raw_path)
    if not raw_path:
        return None
    path = Path(raw_path)
    if not path.is_absolute():
        path = REPO_ROOT / path
    return path


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


def split_table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


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


def section(markdown: str, heading: str, level: int = 2) -> str:
    marker = "#" * level
    next_heading = r"\n#{1,%d} " % level
    pattern = rf"^{re.escape(marker)} {re.escape(heading)}\s*\n(?P<body>.*?)(?:{next_heading}|\Z)"
    match = re.search(pattern, markdown, flags=re.M | re.S)
    return match.group("body").strip() if match else ""


def section_or_placeholder(markdown: str, heading: str, placeholder: str = "Not captured in source artifact.") -> str:
    return section(markdown, heading) or placeholder


def parse_metadata(markdown: str) -> dict[str, str]:
    metadata: dict[str, str] = {}
    metadata_section = section(markdown, "Metadata")
    for row in parse_markdown_table(metadata_section):
        field = row.get("Field", "")
        value = row.get("Value", "")
        if field:
            metadata[field] = clean(value)
    return metadata


def render_template(name: str, context: dict[str, str]) -> str:
    rendered = read_text(TEMPLATE_DIR / name)
    for key, value in context.items():
        rendered = rendered.replace("{{" + key + "}}", value)
    return rendered.rstrip() + "\n"


def summarize_requirements(spec_markdown: str) -> str:
    rows = parse_markdown_table(section(spec_markdown, "Functional Requirements"))
    nfr_rows = parse_markdown_table(section(spec_markdown, "Non-Functional Requirements"))
    lines: list[str] = []

    if rows:
        lines.append(f"- Functional requirements captured: {len(rows)}")
        must_count = sum(1 for row in rows if row.get("Priority", "").lower() == "must")
        if must_count:
            lines.append(f"- Must-priority functional requirements: {must_count}")
        for row in rows[:8]:
            req_id = row.get("Req ID", "Requirement")
            requirement = row.get("Requirement", "")
            lines.append(f"- {req_id}: {requirement}")

    if nfr_rows:
        lines.append(f"- Non-functional requirements captured: {len(nfr_rows)}")
        for row in nfr_rows[:5]:
            req_id = row.get("NFR ID") or row.get("Req ID") or "NFR"
            requirement = row.get("Requirement", "")
            lines.append(f"- {req_id}: {requirement}")

    return "\n".join(lines) if lines else "No requirement table found in source specification."


def summarize_open_conditions(workflow: dict[str, dict[str, str]], validation_markdown: str) -> str:
    pending_gate = workflow.get("pending_gate", {})
    conditions = section(validation_markdown, "Not Yet Validated") or section(validation_markdown, "Defects Or Gaps")
    lines: list[str] = []

    if pending_gate:
        gate = pending_gate.get("gate", "")
        status = pending_gate.get("status", "")
        if gate or status:
            lines.append(f"- Pending gate: {gate or 'unknown'} ({status or 'unknown'})")

    if conditions:
        lines.append(conditions)

    return "\n".join(lines) if lines else "No open conditions captured in source artifacts."


def build_context(workflow_path: Path) -> dict[str, str]:
    workflow = parse_workflow_state(workflow_path)
    capability = workflow.get("capability", {})
    workflow_values = workflow.get("workflow", {})
    artifacts = workflow.get("artifacts", {})

    intent_path = resolve_path(artifacts.get("intent", ""))
    spec_path = resolve_path(artifacts.get("specification", ""))
    context_path = resolve_path(artifacts.get("architecture", ""))
    api_contract_path = resolve_path(artifacts.get("api_contract", ""))
    validation_path = resolve_path(artifacts.get("validation_report", ""))
    traceability_path = resolve_path(artifacts.get("traceability", ""))
    release_notes_path = resolve_path(artifacts.get("release_notes", ""))

    required = [intent_path, spec_path, context_path, validation_path]
    missing = [str(path) for path in required if path is None or not path.exists()]
    if missing:
        raise SystemExit("Missing required artifact(s): " + ", ".join(missing))

    intent_markdown = read_text(intent_path)
    spec_markdown = read_text(spec_path)
    context_markdown = read_text(context_path)
    validation_markdown = read_text(validation_path)
    release_notes = (
        read_text(release_notes_path)
        if release_notes_path is not None and release_notes_path.exists()
        else "Release notes are not available in Git for this workflow state."
    )

    validation_metadata = parse_metadata(validation_markdown)

    return {
        "domain": capability.get("domain", ""),
        "capability": capability.get("name", ""),
        "capability_id": capability.get("capability_id", ""),
        "jira_epic": capability.get("jira_epic", ""),
        "workflow_state": workflow_values.get("current_state", ""),
        "workflow_skill": workflow_values.get("current_skill", ""),
        "intent_path": relative_path(intent_path),
        "spec_path": relative_path(spec_path),
        "context_path": relative_path(context_path),
        "api_contract_path": relative_path(api_contract_path),
        "validation_path": relative_path(validation_path),
        "traceability_path": relative_path(traceability_path),
        "release_notes_path": relative_path(release_notes_path) or "Not available",
        "problem_statement": section_or_placeholder(intent_markdown, "Problem Statement"),
        "desired_outcomes": section_or_placeholder(intent_markdown, "Desired Outcomes"),
        "in_scope": section_or_placeholder(intent_markdown, "In Scope"),
        "out_of_scope": section_or_placeholder(intent_markdown, "Out Of Scope"),
        "requirement_overview": summarize_requirements(spec_markdown),
        "approval_position": section_or_placeholder(intent_markdown, "Human Approval Gate"),
        "architecture_summary": section_or_placeholder(context_markdown, "Architecture Summary"),
        "system_boundary": section_or_placeholder(context_markdown, "System Boundary"),
        "integration_context": section_or_placeholder(context_markdown, "Integration Context"),
        "architecture_decisions": section_or_placeholder(context_markdown, "Proposed Architecture Decisions"),
        "security_control_context": section_or_placeholder(context_markdown, "Security And Control Context"),
        "validation_status": validation_metadata.get("Validation Status", ""),
        "validation_scope": section_or_placeholder(validation_markdown, "Scope Of Validation"),
        "evidence_reviewed": section_or_placeholder(validation_markdown, "Evidence Reviewed"),
        "test_execution_summary": section_or_placeholder(validation_markdown, "Test Execution Summary"),
        "validation_findings": section_or_placeholder(validation_markdown, "Validation Findings"),
        "traceability_check": section_or_placeholder(validation_markdown, "Traceability Check"),
        "release_readiness": section_or_placeholder(validation_markdown, "Release Readiness"),
        "release_notes": release_notes.strip(),
        "open_conditions": summarize_open_conditions(workflow, validation_markdown),
    }


def generate(workflow_path: Path) -> dict[str, str]:
    context = build_context(workflow_path)
    return {
        "capability-summary.md": render_template("capability-summary.md", context),
        "architecture-summary.md": render_template("architecture-summary.md", context),
        "validation-summary.md": render_template("validation-summary.md", context),
        "release-summary.md": render_template("release-summary.md", context),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate offline Confluence summary drafts from AI SDLC artifacts.")
    parser.add_argument("--workflow-state", required=True, type=Path, help="Path to workflow-state.yaml.")
    parser.add_argument("--output-dir", type=Path, help="Optional output directory for generated Markdown summaries.")
    args = parser.parse_args()

    workflow_state_path = args.workflow_state
    if not workflow_state_path.is_absolute():
        workflow_state_path = REPO_ROOT / workflow_state_path
    if not workflow_state_path.exists():
        raise SystemExit(f"Workflow state file not found: {workflow_state_path}")

    summaries = generate(workflow_state_path)

    if args.output_dir:
        args.output_dir.mkdir(parents=True, exist_ok=True)
        for filename, content in summaries.items():
            (args.output_dir / filename).write_text(content, encoding="utf-8")
        print(f"Wrote Confluence summary drafts to {args.output_dir}")
    else:
        for filename, content in summaries.items():
            print(f"--- {filename} ---")
            print(content)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
