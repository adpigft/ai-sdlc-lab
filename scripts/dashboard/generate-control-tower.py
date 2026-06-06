#!/usr/bin/env python3
"""Generate the AI-SDLC Control Tower dashboard data set.

This generator scans Git-owned artifacts only. It does not call Jira,
Confluence, GitHub, or any other external system.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUTPUT = REPO_ROOT / "build" / "dashboard" / "control-tower.json"
TRACEABILITY_FILE = REPO_ROOT / "traceability" / "traceability-matrix.md"
WORKFLOW_MATRIX_FILE = REPO_ROOT / "framework" / "07-control-tower" / "workflow-ownership-matrix.md"

FALLBACK_WORKFLOW_MATRIX = {
    "Candidate Imported": {
        "owner_role": "Delivery Lead",
        "approver_role": "Product Owner",
        "expected_max_days": 2,
    },
    "Intent Draft": {
        "owner_role": "Business Analyst",
        "approver_role": "Product Owner",
        "expected_max_days": 3,
    },
    "Intent Approved": {
        "owner_role": "Business Analyst",
        "approver_role": "Product Owner",
        "expected_max_days": 1,
    },
    "Specification Draft": {
        "owner_role": "Business Analyst",
        "approver_role": "Product Owner",
        "expected_max_days": 4,
    },
    "Specification Approved": {
        "owner_role": "Business Analyst",
        "approver_role": "Product Owner",
        "expected_max_days": 2,
    },
    "Design Approved": {
        "owner_role": "Solution Architect",
        "approver_role": "Solution Architect",
        "expected_max_days": 2,
    },
    "Ready for Build": {
        "owner_role": "Developer Lead",
        "approver_role": "Solution Architect",
        "expected_max_days": 2,
    },
    "In Development": {
        "owner_role": "Developer Lead",
        "approver_role": "Developer Lead",
        "expected_max_days": 5,
    },
    "Validation Passed": {
        "owner_role": "QA Lead",
        "approver_role": "QA Lead",
        "expected_max_days": 3,
    },
    "Release Ready": {
        "owner_role": "DevSecOps / Platform",
        "approver_role": "DevSecOps / Platform",
        "expected_max_days": 2,
    },
    "Released": {
        "owner_role": "Delivery Lead",
        "approver_role": "Delivery Lead",
        "expected_max_days": 0,
    },
}


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def safe_read_text(path: Path) -> str:
    return read_text(path) if path.exists() else ""


def clean(value: str | None) -> str:
    if value is None:
        return ""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'", "`"}:
        value = value[1:-1]
    return value.strip()


def humanize_slug(value: str) -> str:
    value = re.sub(r"[-_]+", " ", value.strip())
    return value.title().strip()


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

    return rows


def parse_workflow_matrix() -> dict[str, dict[str, Any]]:
    if not WORKFLOW_MATRIX_FILE.exists():
        return dict(FALLBACK_WORKFLOW_MATRIX)

    text = read_text(WORKFLOW_MATRIX_FILE)
    match = re.search(r"^## States\s*\n(?P<body>(?:\|.*\n)+)", text, flags=re.M)
    if not match:
        return dict(FALLBACK_WORKFLOW_MATRIX)

    try:
        rows = parse_markdown_table(match.group("body"))
        matrix: dict[str, dict[str, Any]] = {}
        for row in rows:
            state = clean(row.get("State", ""))
            if not state:
                continue
            max_days = row.get("Expected Max Days", "")
            matrix[state] = {
                "owner_role": clean(row.get("Owner Role", "")) or None,
                "approver_role": clean(row.get("Approver Role", "")) or None,
                "expected_max_days": int(clean(max_days)) if clean(max_days).isdigit() else None,
            }

        if not matrix:
            return dict(FALLBACK_WORKFLOW_MATRIX)
        return matrix
    except Exception:
        return dict(FALLBACK_WORKFLOW_MATRIX)


def extract_metadata(markdown: str) -> dict[str, str]:
    match = re.search(r"^## Metadata\s*\n(?P<body>.*?)(?:\n## |\Z)", markdown, flags=re.M | re.S)
    if not match:
        return {}

    metadata: dict[str, str] = {}
    for row in parse_markdown_table(match.group("body")):
        field = row.get("Field", "")
        value = row.get("Value", "")
        if field:
            metadata[field] = clean(value)
    return metadata


def extract_heading(markdown: str) -> str:
    match = re.search(r"^#\s+(?P<title>.+)$", markdown, flags=re.M)
    return clean(match.group("title")) if match else ""


def strip_artifact_suffix(value: str) -> str:
    value = clean(value)
    value = re.sub(
        r"\s+(Intent|Specification|Design|Test(?: Case)?|Validation(?: Report)?|Release(?: Notes)?)$",
        "",
        value,
        flags=re.I,
    )
    return clean(value)


def extract_section(markdown: str, heading: str, level: int = 2) -> str:
    marker = "#" * level
    next_heading = r"\n#{1,%d} " % level
    pattern = rf"^{re.escape(marker)} {re.escape(heading)}\s*\n(?P<body>.*?)(?:{next_heading}|\Z)"
    match = re.search(pattern, markdown, flags=re.M | re.S)
    return match.group("body").strip() if match else ""


def extract_first_paragraph(markdown: str, heading: str, level: int = 2) -> str:
    body = extract_section(markdown, heading, level=level)
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", body) if part.strip()]
    return paragraphs[0] if paragraphs else ""


def normalize(value: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", "", clean(value).lower())


def git_last_modified(path: Path) -> datetime:
    if not path.exists():
        return datetime.fromtimestamp(0, tz=timezone.utc)

    try:
        completed = subprocess.run(
            ["git", "log", "-1", "--format=%ct", "--", str(path.relative_to(REPO_ROOT))],
            check=False,
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        timestamp = int(completed.stdout.strip() or "0")
        if timestamp > 0:
            return datetime.fromtimestamp(timestamp, tz=timezone.utc)
    except (ValueError, OSError):
        pass

    return datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)


def days_in_state(artifact_path: Path) -> int:
    delta = datetime.now(timezone.utc) - git_last_modified(artifact_path)
    return max(delta.days, 0)


def last_updated_for(paths: list[Path], fallback: datetime) -> str:
    for path in paths:
        if path.exists() and path.is_file():
            return git_last_modified(path).isoformat()
    return fallback.isoformat()


def relative_path(path: Path | None) -> str:
    if path is None:
        return ""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def read_workflow_state(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}

    state: dict[str, Any] = {"raw": {}}
    current_section = ""
    current_nested = ""

    for raw_line in read_text(path).splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if not line.startswith(" "):
            current_nested = ""
        if not line.startswith(" ") and line.endswith(":"):
            current_section = line[:-1].strip()
            state[current_section] = {}
            continue
        if current_section and line.startswith("  ") and line.rstrip().endswith(":"):
            current_nested = line.strip()[:-1]
            state[current_section][current_nested] = {}
            continue
        match = re.match(r"^(\s{2,})([A-Za-z0-9_]+):\s*(.*)$", line)
        if match and current_section:
            indent = len(match.group(1))
            key = match.group(2)
            value = clean(match.group(3))
            if indent >= 4 and current_nested and isinstance(state[current_section].get(current_nested), dict):
                state[current_section][current_nested][key] = value
            else:
                state[current_section][key] = value
    return state


def parse_traceability() -> list[dict[str, Any]]:
    if not TRACEABILITY_FILE.exists():
        return []

    text = read_text(TRACEABILITY_FILE)
    lines = text.splitlines()
    rows: list[dict[str, Any]] = []
    current_section = ""
    current_traceability_id = ""
    index = 0

    while index < len(lines):
        line = lines[index].rstrip()
        section_match = re.match(r"^##\s+(?P<title>.+)$", line)
        if section_match:
            current_section = clean(section_match.group("title"))
            current_traceability_id = ""
            index += 1
            while index < len(lines) and not lines[index].startswith("## "):
                id_match = re.match(r"^Traceability ID:\s*(.+)$", lines[index].strip())
                if id_match:
                    current_traceability_id = clean(id_match.group(1))
                if lines[index].strip().startswith("|") and index + 1 < len(lines):
                    header = split_table_row(lines[index])
                    separator = split_table_row(lines[index + 1]) if index + 1 < len(lines) else []
                    if header and separator and all(re.fullmatch(r":?-{2,}:?", cell.strip()) for cell in separator):
                        index += 2
                        while index < len(lines):
                            row_line = lines[index].rstrip()
                            if not row_line.strip().startswith("|"):
                                break
                            cells = split_table_row(row_line)
                            if len(cells) != len(header):
                                break
                            row = {header[column]: clean(cells[column]) for column in range(len(header))}
                            row["_section"] = current_section
                            row["_traceability_id"] = current_traceability_id
                            rows.append(row)
                            index += 1
                        continue
                index += 1
            continue
        index += 1

    return rows


def pick_metadata_value(*values: str) -> str:
    for value in values:
        cleaned = clean(value)
        if cleaned and normalize(cleaned) not in {"tbd", "todo", "draft", "n_a", "na", "unknown"}:
            return cleaned
    return clean(values[0]) if values else ""


def artifact_exists(path: Path | None) -> bool:
    return bool(path and path.exists() and path.is_file())


def feature_owner_role(intent_meta: dict[str, str], spec_meta: dict[str, str], workflow_state: dict[str, Any]) -> str:
    current_artifact = workflow_state.get("current_artifact", {})
    if isinstance(current_artifact, dict):
        role = pick_metadata_value(current_artifact.get("owner_role", ""))
        if role:
            return role
    owner = pick_metadata_value(spec_meta.get("Owner", ""), intent_meta.get("Owner", ""))
    if owner:
        return owner
    stakeholder = pick_metadata_value(intent_meta.get("Capability"), intent_meta.get("Domain"))
    return stakeholder


def is_approval_state(state: str) -> bool:
    normalized = normalize(state)
    return normalized in {
        "intentapproved",
        "specificationapproved",
        "designapproved",
        "readyforbuild",
        "validationpassed",
        "releaseready",
    }


def governance_state_for_feature(
    intent_meta: dict[str, str],
    spec_meta: dict[str, str],
    design_meta: dict[str, str],
    validation_status: str,
    intent_exists: bool,
    spec_exists: bool,
    design_exists: bool,
    tests_exists: bool,
    validation_exists: bool,
    release_exists: bool,
) -> str:
    if not intent_exists:
        return "Candidate Imported"

    intent_status = normalize(intent_meta.get("Status", ""))
    spec_status = normalize(spec_meta.get("Status", ""))
    design_status = normalize(design_meta.get("Status", ""))
    validation_status_norm = normalize(validation_status)

    if not spec_exists:
        return "Intent Approved" if "approved" in intent_status else "Intent Draft"

    if not design_exists:
        return "Specification Approved" if "approved" in spec_status else "Specification Draft"

    if release_exists and validation_status_norm.startswith("pass"):
        return "Released"
    if release_exists:
        return "Release Ready"
    if validation_exists and (validation_status_norm.startswith("pass") or validation_status_norm.startswith("complete")):
        return "Validation Passed"
    if tests_exists:
        return "In Development"
    if "approved" in design_status:
        return "Design Approved"
    return "Ready for Build"


def determine_state(
    intent_meta: dict[str, str],
    spec_meta: dict[str, str],
    design_meta: dict[str, str],
    workflow_state: dict[str, Any],
    intent_exists: bool,
    spec_exists: bool,
    design_exists: bool,
    tests_exists: bool,
    validation_exists: bool,
    release_exists: bool,
) -> tuple[str, str, str, bool]:
    if workflow_state:
        current_state = clean(workflow_state.get("workflow", {}).get("current_state", ""))
        blocked = str(workflow_state.get("workflow", {}).get("blocked", "")).lower() == "true"
        pending_gate = workflow_state.get("pending_gate", {})
        next_gate = clean(pending_gate.get("gate", "")) if isinstance(pending_gate, dict) else ""
        if not next_gate:
            next_skill = clean(workflow_state.get("workflow", {}).get("next_skill", ""))
            next_gate = humanize_slug(next_skill.replace("_", " ")) if next_skill else "Unknown"
        return (humanize_slug(current_state), next_gate or "Unknown", clean(workflow_state.get("workflow", {}).get("blocked_reason", "")), blocked)

    spec_status = clean(spec_meta.get("Status", ""))
    intent_status = clean(intent_meta.get("Status", ""))
    blocked = "blocked" in normalize(spec_status) or "blocked" in normalize(intent_status)

    if not intent_exists:
        return ("Intent Missing", "Intent Approval", "", blocked)
    if not spec_exists:
        return (humanize_slug(intent_status or "Intent Approved"), "Specification Review", "", blocked)
    normalized_design = normalize(design_meta.get("Status", ""))
    normalized_spec = normalize(spec_status)
    if design_exists:
        if "draft" in normalized_design:
            base_state = clean(design_meta.get("Status", "Draft for Architect Review"))
            next_gate = "Architect Review"
        elif "approved" in normalized_design:
            base_state = clean(design_meta.get("Status", "Design Approved"))
            next_gate = "Test Design Review" if not tests_exists else "Validation Review" if not validation_exists else "Release Review"
        else:
            base_state = clean(design_meta.get("Status", "")) or "Design Ready"
            next_gate = "Architect Review"
        return (base_state, next_gate, "", blocked)
    if "draft" in normalized_spec:
        base_state = "Specification Draft"
    elif "approved" in normalized_spec:
        base_state = "Specification Approved"
    else:
        base_state = spec_status or "Specification Draft"
    return (base_state, "Design Review", "", blocked)


def derive_feature_id(intent_meta: dict[str, str], spec_meta: dict[str, str], feature_slug: str) -> str:
    for candidate in (
        intent_meta.get("Feature ID", ""),
        spec_meta.get("Feature ID", ""),
        spec_meta.get("Spec ID", ""),
        intent_meta.get("Intent ID", ""),
    ):
        candidate = clean(candidate)
        if candidate:
            if candidate.startswith("SPEC-"):
                return "FEAT-" + candidate[len("SPEC-") :]
            if candidate.startswith("INT-"):
                return "FEAT-" + candidate[len("INT-") :]
            if candidate.startswith("FEAT-"):
                return candidate
    slug = re.sub(r"[^A-Za-z0-9]+", "-", feature_slug.upper()).strip("-")
    return f"FEAT-{slug or 'UNKNOWN'}"


def parse_validation_status(path: Path) -> tuple[str, str]:
    if not path.exists():
        return ("Not available", "")

    markdown = read_text(path)
    metadata = extract_metadata(markdown)
    status = pick_metadata_value(metadata.get("Validation Status", ""), metadata.get("Status", ""))
    evidence = pick_metadata_value(
        metadata.get("GitHub Actions Evidence", ""),
        metadata.get("GitHub Validation Evidence", ""),
        metadata.get("Validation Evidence", ""),
    )
    summary = extract_first_paragraph(markdown, "Release Readiness") or extract_first_paragraph(markdown, "Validation Findings")
    if evidence and summary:
        summary = f"{summary} | GitHub evidence: {evidence}"
    elif evidence:
        summary = f"GitHub evidence: {evidence}"
    return (status or "Not available", summary)


def has_openapi(path: Path) -> bool:
    return path.exists() and path.is_file()


def git_url(base_url: str, key: str) -> str:
    return f"{base_url.rstrip('/')}/browse/{key}"


def confluence_url(base_url: str, space_key: str, page_id: str) -> str:
    return f"{base_url.rstrip('/')}/spaces/{space_key}/pages/{page_id}"


def build_feature_record(
    domain_dir: Path,
    capability_dir: Path,
    feature_dir: Path,
    trace_rows: list[dict[str, Any]],
    workflow_matrix: dict[str, dict[str, Any]],
    generated_at: datetime,
) -> dict[str, Any]:
    intent_path = feature_dir / "intent" / "intent.md"
    spec_path = feature_dir / "specification" / "specification.md"
    design_path = feature_dir / "design" / "design.md"
    tests_path = feature_dir / "tests" / "acceptance.feature"
    implementation_plan_path = feature_dir / "implementation" / "implementation-plan.md"
    validation_report_path = feature_dir / "validation" / "validation-report.md"
    release_notes_path = feature_dir / "release" / "release-notes.md"
    openapi_path = feature_dir / "contracts" / "openapi.yaml"
    workflow_state_path = feature_dir / "workflow-state.yaml"

    intent_exists = artifact_exists(intent_path)
    spec_exists = artifact_exists(spec_path)
    design_exists = artifact_exists(design_path)
    tests_exists = artifact_exists(tests_path)
    validation_exists = artifact_exists(validation_report_path)
    release_exists = artifact_exists(release_notes_path)
    openapi_exists = artifact_exists(openapi_path)

    intent_markdown = safe_read_text(intent_path)
    spec_markdown = safe_read_text(spec_path)
    design_markdown = safe_read_text(design_path)
    validation_markdown = safe_read_text(validation_report_path)
    workflow_state = read_workflow_state(workflow_state_path)
    intent_meta = extract_metadata(intent_markdown)
    spec_meta = extract_metadata(spec_markdown)
    design_meta = extract_metadata(design_markdown)
    validation_meta = extract_metadata(validation_markdown)

    feature_name = pick_metadata_value(
        strip_artifact_suffix(intent_meta.get("Feature", "")),
        strip_artifact_suffix(spec_meta.get("Feature", "")),
        strip_artifact_suffix(extract_heading(intent_markdown)),
        strip_artifact_suffix(extract_heading(spec_markdown)),
        humanize_slug(feature_dir.name),
    )
    capability_name = pick_metadata_value(intent_meta.get("Capability", ""), spec_meta.get("Capability", ""), humanize_slug(capability_dir.name))
    domain_name = pick_metadata_value(intent_meta.get("Domain", ""), spec_meta.get("Domain", ""), humanize_slug(domain_dir.name))
    feature_slug = feature_dir.name
    feature_id = derive_feature_id(intent_meta, spec_meta, feature_slug)
    intent_id = pick_metadata_value(intent_meta.get("Intent ID", ""))
    spec_id = pick_metadata_value(spec_meta.get("Spec ID", ""))
    design_id = pick_metadata_value(design_meta.get("Design ID", design_meta.get("Architecture ID", "")))
    test_id = derive_test_id(spec_meta, feature_slug)
    owner_role = feature_owner_role(intent_meta, spec_meta, workflow_state)

    state, next_gate, blocked_reason, blocked = determine_state(
        intent_meta,
        spec_meta,
        design_meta,
        workflow_state,
        intent_exists,
        spec_exists,
        design_exists,
        tests_exists,
        validation_exists,
        release_exists,
    )

    primary_path = workflow_state_path if workflow_state_path.exists() else (spec_path if spec_path.exists() else intent_path)
    if not primary_path.exists() and design_path.exists():
        primary_path = design_path
    days_state = days_in_state(primary_path)
    workflow_last_updated = last_updated_for([workflow_state_path, primary_path], generated_at)

    trace_row = match_traceability_row(trace_rows, feature_dir, intent_meta, spec_meta)
    traceability_id = clean(trace_row.get("_traceability_id", "")) if trace_row else ""
    jira_key = pick_metadata_value(trace_row.get("Jira", "") if trace_row else "", workflow_state.get("capability", {}).get("jira_epic", ""))
    confluence_page_id = pick_metadata_value(trace_row.get("Confluence", "") if trace_row else "", workflow_state.get("feature", {}).get("confluence_page", ""))

    validation_status, validation_summary = parse_validation_status(validation_report_path)
    governance_state = governance_state_for_feature(
        intent_meta,
        spec_meta,
        design_meta,
        validation_status,
        intent_exists,
        spec_exists,
        design_exists,
        tests_exists,
        validation_exists,
        release_exists,
    )
    matrix_defaults = workflow_matrix.get(governance_state) or FALLBACK_WORKFLOW_MATRIX.get(governance_state, {})
    if not matrix_defaults and normalize(state) in {
        "intentapproved",
        "specificationapproved",
        "designapproved",
        "readyforbuild",
        "validationpassed",
        "releaseready",
    }:
        matrix_defaults = FALLBACK_WORKFLOW_MATRIX.get(state, {})

    expected_max_days = matrix_defaults.get("expected_max_days")
    if not isinstance(expected_max_days, int):
        expected_max_days = None

    workflow_owner_role = clean(matrix_defaults.get("owner_role")) or None
    workflow_approver_role = clean(matrix_defaults.get("approver_role")) or None
    if not workflow_owner_role:
        workflow_owner_role = owner_role or None
    if workflow_approver_role is None and governance_state and is_approval_state(governance_state):
        workflow_approver_role = None

    quality = {
        "intentPresent": intent_exists,
        "specificationPresent": spec_exists,
        "designPresent": design_exists,
        "testsPresent": tests_exists,
        "openapiPresent": openapi_exists,
        "traceabilityPresent": bool(traceability_id),
        "validationStatus": validation_status,
        "validationSummary": validation_summary,
        "releaseReadinessStatus": "Ready" if release_exists and ("ready" in normalize(validation_status) or "passed" in normalize(validation_status)) else "Not ready",
    }

    jira_base_url = os.getenv("JIRA_BASE_URL", "").strip() or os.getenv("JIRA_SITE_URL", "").strip()
    confluence_base_url = os.getenv("CONFLUENCE_BASE_URL", "").strip()
    if not confluence_base_url and jira_base_url:
        confluence_base_url = f"{jira_base_url.rstrip('/')}/wiki"
    confluence_space_key = os.getenv("CONFLUENCE_SPACE_KEY", "").strip()

    links = {
        "gitIntentPath": relative_path(intent_path) if intent_exists else "",
        "gitSpecificationPath": relative_path(spec_path) if spec_exists else "",
        "gitDesignPath": relative_path(design_path) if design_exists else "",
        "gitTestsPath": relative_path(tests_path) if tests_exists else "",
        "gitValidationPath": relative_path(validation_report_path) if validation_exists else "",
        "gitReleasePath": relative_path(release_notes_path) if release_exists else "",
        "jiraUrl": git_url(jira_base_url, jira_key) if jira_base_url and jira_key else "",
        "confluenceUrl": confluence_url(confluence_base_url, confluence_space_key, confluence_page_id) if confluence_base_url and confluence_space_key and confluence_page_id else "",
    }

    intervention_reasons: list[str] = []
    if blocked:
        intervention_reasons.append("blocked")
    if expected_max_days is not None and days_state > expected_max_days:
        intervention_reasons.append("stale-state")
    if not workflow_owner_role or normalize(workflow_owner_role) in {"tbd", "unknown"}:
        intervention_reasons.append("missing-owner")
    if is_approval_state(governance_state) and (not workflow_approver_role or normalize(workflow_approver_role) in {"tbd", "unknown"}):
        intervention_reasons.append("missing-approval")
    if validation_status and ("fail" in normalize(validation_status) or "blocked" in normalize(validation_status) or "notready" in normalize(validation_status)):
        intervention_reasons.append("failed-validation")
    if not traceability_id:
        intervention_reasons.append("missing-traceability")
    if not jira_key or not confluence_page_id:
        intervention_reasons.append("sync-missing")

    interventions = []
    for reason in intervention_reasons:
        if reason not in interventions:
            interventions.append(reason)

    focus = normalize(feature_name) == "cardreplacement" or normalize(feature_slug) == "cardreplacement"
    workflow = {
        "state": state,
        "owner_role": owner_role or workflow_owner_role,
        "approver_role": (
            clean(workflow_state.get("current_artifact", {}).get("approver_role", ""))
            if isinstance(workflow_state.get("current_artifact", {}), dict)
            and clean(workflow_state.get("current_artifact", {}).get("approver_role", ""))
            else workflow_approver_role
        ) or None,
        "next_gate": next_gate,
        "blocked_reason": blocked_reason,
        "days_in_state": days_state,
        "last_updated": workflow_last_updated,
        "expected_max_days": expected_max_days,
        "pm_intervention_trigger": bool(intervention_reasons),
    }

    return {
        "domain": domain_name,
        "capability": capability_name,
        "feature": feature_name,
        "featureId": feature_id,
        "intentId": intent_id,
        "specId": spec_id,
        "designId": design_id,
        "testId": test_id,
        "state": state,
        "ownerRole": owner_role,
        "daysInState": days_state,
        "blocked": blocked,
        "blockedReason": blocked_reason,
        "nextGate": next_gate,
        "workflow": workflow,
        "jiraKey": jira_key,
        "confluencePageId": confluence_page_id,
        "traceabilityId": traceability_id,
        "focus": focus,
        "quality": quality,
        "links": links,
        "interventions": interventions,
        "paths": {
            "intent": relative_path(intent_path) if intent_exists else "",
            "specification": relative_path(spec_path) if spec_exists else "",
            "design": relative_path(design_path) if design_exists else "",
            "tests": relative_path(tests_path) if tests_exists else "",
            "validation": relative_path(validation_report_path) if validation_exists else "",
            "release": relative_path(release_notes_path) if release_exists else "",
            "workflowState": relative_path(workflow_state_path) if workflow_state_path.exists() else "",
            "openapi": relative_path(openapi_path) if openapi_exists else "",
        },
        "evidence": {
            "validationReport": relative_path(validation_report_path) if validation_exists else "",
            "validationStatus": validation_status,
            "validationSummary": validation_summary,
            "githubValidationEvidence": validation_meta.get("GitHub Actions Evidence", "") if validation_meta else "",
        },
    }


def match_traceability_row(
    rows: list[dict[str, Any]],
    feature_dir: Path,
    intent_meta: dict[str, str],
    spec_meta: dict[str, str],
) -> dict[str, Any] | None:
    spec_path = relative_path(feature_dir / "specification" / "specification.md")
    intent_id = clean(intent_meta.get("Intent ID", ""))
    feature_name = normalize(intent_meta.get("Feature", "")) or normalize(spec_meta.get("Feature", ""))

    for row in rows:
        row_text = " ".join(str(value) for key, value in row.items() if not key.startswith("_"))
        if spec_path and spec_path in row_text:
            return row
        if intent_id and intent_id in row_text:
            return row
        if feature_name and feature_name in normalize(row_text):
            return row
    return None


def derive_test_id(spec_meta: dict[str, str], feature_slug: str) -> str:
    for candidate in (
        spec_meta.get("Test ID", ""),
        spec_meta.get("Validation Test ID", ""),
        spec_meta.get("Validation Plan ID", ""),
        spec_meta.get("Spec ID", ""),
        spec_meta.get("Intent ID", ""),
    ):
        candidate = clean(candidate)
        if candidate:
            if candidate.startswith("SPEC-"):
                return "TEST-" + candidate[len("SPEC-") :]
            if candidate.startswith("INT-"):
                return "TEST-" + candidate[len("INT-") :]
            if candidate.startswith("TEST-"):
                return candidate
    slug = re.sub(r"[^A-Za-z0-9]+", "-", feature_slug.upper()).strip("-")
    return f"TEST-{slug or 'UNKNOWN'}"


def parse_features(generated_at: datetime, workflow_matrix: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    trace_rows = parse_traceability()
    features: list[dict[str, Any]] = []

    for domain_dir in sorted([path for path in (REPO_ROOT / "domains").iterdir() if path.is_dir()]):
        capabilities_dir = domain_dir / "capabilities"
        if not capabilities_dir.exists():
            continue
        for capability_dir in sorted([path for path in capabilities_dir.iterdir() if path.is_dir()]):
            features_dir = capability_dir / "features"
            if not features_dir.exists():
                continue
            for feature_dir in sorted([path for path in features_dir.iterdir() if path.is_dir()]):
                record = build_feature_record(domain_dir, capability_dir, feature_dir, trace_rows, workflow_matrix, generated_at)
                if record["feature"]:
                    features.append(record)

    features.sort(key=lambda item: (0 if item.get("focus") else 1, item["domain"], item["capability"], item["feature"]))
    return features


def summarize(features: list[dict[str, Any]], generated_at: datetime) -> dict[str, Any]:
    states: dict[str, int] = {}
    approval_queue: dict[str, int] = {
        "PO / BA review": 0,
        "QA review": 0,
        "SA review": 0,
        "Dev review": 0,
        "DevOps / release review": 0,
    }
    blocked_count = 0
    validation_passed = 0
    validation_failed = 0
    traced = 0
    release_ready = 0

    def queue_for(feature: dict[str, Any]) -> str:
        state = normalize(feature.get("state", ""))
        next_gate = clean(feature.get("nextGate", ""))
        if feature.get("blocked"):
            return "Dev review"
        if "intent" in state or "draft" in state or "po" in normalize(next_gate) or "ba" in normalize(next_gate):
            return "PO / BA review"
        if "design" in state or "architect" in normalize(next_gate) or "sa" in normalize(next_gate):
            return "SA review"
        if "test" in state or "qa" in normalize(next_gate):
            return "QA review"
        if "implementation" in state or "dev" in normalize(next_gate):
            return "Dev review"
        return "DevOps / release review"

    for feature in features:
        state = feature.get("state", "Unknown")
        states[state] = states.get(state, 0) + 1
        if feature.get("blocked"):
            blocked_count += 1
        if feature.get("traceabilityId"):
            traced += 1
        validation_status = normalize(feature.get("quality", {}).get("validationStatus", ""))
        if validation_status.startswith("pass") or validation_status.startswith("complete"):
            validation_passed += 1
        elif validation_status and (
            "fail" in validation_status or "blocked" in validation_status or "notready" in validation_status or "partial" in validation_status
        ):
            validation_failed += 1
        if feature.get("quality", {}).get("releaseReadinessStatus") == "Ready":
            release_ready += 1
        approval_queue[queue_for(feature)] += 1

    coverage = round((traced / len(features) * 100) if features else 0.0, 1)

    return {
        "generatedAt": generated_at.isoformat(),
        "summary": {
            "totalFeatures": len(features),
            "blockedFeatures": blocked_count,
            "validationPassed": validation_passed,
            "validationFailed": validation_failed,
            "traceabilityCoveragePercent": coverage,
            "releaseReadyFeatures": release_ready,
            "featuresByState": dict(sorted(states.items(), key=lambda item: (-item[1], item[0]))),
        },
        "approvalQueue": approval_queue,
        "features": features,
    }


def write_json(data: dict[str, Any], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate the AI-SDLC Control Tower dashboard data set")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Path to control-tower.json")
    args = parser.parse_args(argv)

    generated_at = datetime.now(timezone.utc)
    workflow_matrix = parse_workflow_matrix()
    features = parse_features(generated_at, workflow_matrix)
    data = summarize(features, generated_at)
    write_json(data, Path(args.output).expanduser().resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
