#!/usr/bin/env python3
"""REST/CLI demo adapters for Jira Cloud.

This script validates Jira connectivity, drafts a story from an approved intent,
adds synchronized source links, and transitions issue status when explicitly
allowed. It uses environment variables only and does not write unless
`--apply` is supplied.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import re
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


REPO_ROOT = Path(__file__).resolve().parents[2]


def env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def optional_env(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


def clean(value: str | None) -> str:
    if value is None:
        return ""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'", "`"}:
        value = value[1:-1]
    return value.strip()


def normalize(value: str | None) -> str:
    return re.sub(r"[^a-z0-9]+", "", clean(value).lower())


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


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


def section(markdown: str, heading: str, level: int = 2) -> str:
    marker = "#" * level
    next_heading = r"\n#{1,%d} " % level
    pattern = rf"^{re.escape(marker)} {re.escape(heading)}\s*\n(?P<body>.*?)(?:{next_heading}|\Z)"
    match = re.search(pattern, markdown, flags=re.M | re.S)
    return match.group("body").strip() if match else ""


def first_paragraph(markdown: str, heading: str) -> str:
    body = section(markdown, heading)
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", body) if part.strip()]
    return paragraphs[0] if paragraphs else ""


def relative_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def jira_base_url() -> str:
    return env("JIRA_BASE_URL").rstrip("/")


def jira_api_url(path: str) -> str:
    return f"{jira_base_url()}{path}"


def auth_header() -> str:
    token = f"{env('JIRA_EMAIL')}:{env('JIRA_API_TOKEN')}".encode("utf-8")
    return "Basic " + base64.b64encode(token).decode("ascii")


def request_json(method: str, url: str, payload: dict[str, Any] | None = None) -> tuple[int, Any, dict[str, str]]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    headers = {
        "Accept": "application/json",
        "Authorization": auth_header(),
    }
    if payload is not None:
        headers["Content-Type"] = "application/json"

    request = Request(url, data=data, headers=headers, method=method)
    try:
        with urlopen(request) as response:
            raw = response.read().decode("utf-8")
            parsed = json.loads(raw) if raw else None
            return response.status, parsed, dict(response.headers.items())
    except HTTPError as error:
        raw = error.read().decode("utf-8", errors="replace")
        raise SystemExit(f"{method} {url} failed: {error.code} {error.reason}\n{raw}") from error
    except URLError as error:
        raise SystemExit(f"{method} {url} failed: {error.reason}") from error


def load_intent(path: Path) -> dict[str, Any]:
    markdown = read_text(path)
    metadata = {row.get("Field", ""): clean(row.get("Value", "")) for row in parse_markdown_table(section(markdown, "Metadata"))}
    gate_rows = parse_markdown_table(section(markdown, "Human Gate"))
    gate_row = next((row for row in gate_rows if row.get("Approval", "").lower().startswith("product intent")), gate_rows[0] if gate_rows else {})
    problem_statement = first_paragraph(markdown, "Problem Statement")
    desired_outcome = section(markdown, "Desired Outcome")
    scope = section(markdown, "Scope")
    in_scope = section(scope, "In Scope", level=3)
    out_of_scope = section(scope, "Out Of Scope", level=3)

    return {
        "markdown": markdown,
        "metadata": metadata,
        "gate": gate_row,
        "problem_statement": problem_statement,
        "desired_outcome": desired_outcome,
        "in_scope": in_scope,
        "out_of_scope": out_of_scope,
    }


def approved_intent(intent: dict[str, Any]) -> bool:
    metadata_status = normalize(intent["metadata"].get("Status"))
    gate_decision = normalize(intent["gate"].get("Decision"))
    return metadata_status == "approved" or gate_decision == "approved"


def text_to_adf(text: str) -> dict[str, Any]:
    blocks: list[dict[str, Any]] = []
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text.strip()) if part.strip()]
    if not paragraphs:
        paragraphs = [""]

    for paragraph in paragraphs:
        lines = paragraph.splitlines()
        content = []
        for index, line in enumerate(lines):
            if line:
                content.append({"type": "text", "text": line})
            if index < len(lines) - 1:
                content.append({"type": "hardBreak"})
        blocks.append({"type": "paragraph", "content": content or [{"type": "text", "text": ""}]})

    return {"type": "doc", "version": 1, "content": blocks}


def description_from_intent(intent_path: Path, intent: dict[str, Any]) -> dict[str, Any]:
    metadata = intent["metadata"]
    sections = [
        ("Intent", f"Intent ID: {metadata.get('Intent ID', '')}\nJira Epic: {metadata.get('Jira Epic', '')}\nCapability: {metadata.get('Capability', '')}\nDomain: {metadata.get('Domain', '')}\nStatus: {metadata.get('Status', '')}"),
        ("Problem Statement", intent["problem_statement"]),
        ("Desired Outcome", intent["desired_outcome"]),
        ("In Scope", intent["in_scope"]),
        ("Out Of Scope", intent["out_of_scope"]),
        ("Human Gate", f"Approval: {intent['gate'].get('Approval', '')}\nDecision: {intent['gate'].get('Decision', '')}\nApprover: {intent['gate'].get('Approver', '')}\nDate: {intent['gate'].get('Date', '')}"),
        ("Source Artifact", f"Git source: {relative_path(intent_path)}"),
    ]

    body = []
    for heading, text in sections:
        body.append({"type": "heading", "attrs": {"level": 2}, "content": [{"type": "text", "text": heading}]})
        body.extend(text_to_adf(text)["content"])
    return {"type": "doc", "version": 1, "content": body}


def summary_from_intent(intent: dict[str, Any]) -> str:
    capability = clean(intent["metadata"].get("Capability")) or "Demo Story"
    problem = clean(intent["problem_statement"])
    if problem:
        sentence = re.split(r"(?<=[.!?])\s+", problem)[0]
    else:
        sentence = "Approved intent from Git-backed delivery artifacts."
    summary = f"{capability}: {sentence}".strip()
    return summary[:255]


def validate_connection_project() -> None:
    status, myself, _ = request_json("GET", jira_api_url("/rest/api/3/myself"))
    _, project, _ = request_json("GET", jira_api_url(f"/rest/api/3/project/{quote(env('JIRA_PROJECT_KEY'))}"))
    _, issue_types, _ = request_json(
        "GET",
        jira_api_url(f"/rest/api/3/issue/createmeta/{quote(env('JIRA_PROJECT_KEY'))}/issuetypes"),
    )

    issue_type_items: list[dict[str, Any]] = []
    if isinstance(issue_types, dict):
        candidate_items = issue_types.get("values") or issue_types.get("issueTypes") or []
        if isinstance(candidate_items, list):
            issue_type_items = [item for item in candidate_items if isinstance(item, dict)]
    elif isinstance(issue_types, list):
        issue_type_items = [item for item in issue_types if isinstance(item, dict)]

    names = [item.get("name", "") for item in issue_type_items]
    result = {
        "mode": "validate-connection-project",
        "authenticatedUser": myself.get("displayName") if isinstance(myself, dict) else None,
        "project": {
            "key": project.get("key") if isinstance(project, dict) else env("JIRA_PROJECT_KEY"),
            "name": project.get("name") if isinstance(project, dict) else None,
        },
        "storyIssueTypeAvailable": "Story" in names,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


def create_demo_story(args: argparse.Namespace) -> None:
    intent_path = Path(args.intent).expanduser().resolve()
    if not intent_path.exists():
        raise SystemExit(f"Intent file not found: {intent_path}")

    intent = load_intent(intent_path)
    if not approved_intent(intent):
        raise SystemExit("Intent is not approved. Refusing to create a Jira story draft.")

    payload = {
        "fields": {
            "project": {"key": env("JIRA_PROJECT_KEY")},
            "summary": clean(args.summary) or summary_from_intent(intent),
            "issuetype": {"name": "Story"},
            "labels": ["ai-sdlc", "demo", "rest-cli", "intent-approved"],
            "description": description_from_intent(intent_path, intent),
        }
    }

    if not args.apply:
        print(json.dumps({"mode": "dry-run", "action": "create-demo-story", "payload": payload}, indent=2, ensure_ascii=False))
        return

    status, response, _ = request_json("POST", jira_api_url("/rest/api/3/issue"), payload)
    print(
        json.dumps(
            {
                "mode": "applied",
                "status": status,
                "issueKey": response.get("key") if isinstance(response, dict) else None,
                "issueUrl": response.get("self") if isinstance(response, dict) else None,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


def add_links(args: argparse.Namespace) -> None:
    issue_key = clean(args.issue_key)
    if not issue_key:
        raise SystemExit("--issue-key is required")

    links: list[dict[str, Any]] = []
    if args.git_url:
        links.append(
            {
                "object": {"url": args.git_url, "title": clean(args.git_title) or "Git source artifact"},
                "globalId": f"ai-sdlc:git:{issue_key}:{args.git_url}",
            }
        )
    if args.confluence_url:
        links.append(
            {
                "object": {"url": args.confluence_url, "title": clean(args.confluence_title) or "Confluence published view"},
                "globalId": f"ai-sdlc:confluence:{issue_key}:{args.confluence_url}",
            }
        )

    if not links:
        raise SystemExit("At least one of --git-url or --confluence-url must be provided")

    if not args.apply:
        print(json.dumps({"mode": "dry-run", "action": "add-links", "issueKey": issue_key, "links": links}, indent=2, ensure_ascii=False))
        return

    responses: list[dict[str, Any]] = []
    for link in links:
        _, response, _ = request_json("POST", jira_api_url(f"/rest/api/3/issue/{quote(issue_key)}/remotelink"), link)
        responses.append(response if isinstance(response, dict) else {"response": response})

    print(json.dumps({"mode": "applied", "issueKey": issue_key, "responses": responses}, indent=2, ensure_ascii=False))


def transition_status(args: argparse.Namespace) -> None:
    issue_key = clean(args.issue_key)
    if not issue_key:
        raise SystemExit("--issue-key is required")

    _, response, _ = request_json("GET", jira_api_url(f"/rest/api/3/issue/{quote(issue_key)}/transitions"))
    transitions = response.get("transitions", []) if isinstance(response, dict) else []
    target = clean(args.transition)
    target_status = clean(args.to_status)

    selected = None
    for transition in transitions:
        name = clean(transition.get("name"))
        to_name = clean((transition.get("to") or {}).get("name")) if isinstance(transition.get("to"), dict) else ""
        if target and normalize(name) == normalize(target):
            selected = transition
            break
        if target_status and normalize(to_name) == normalize(target_status):
            selected = transition
            break

    if not selected:
        available = [
            {"id": transition.get("id"), "name": transition.get("name"), "to": (transition.get("to") or {}).get("name")}
            for transition in transitions
        ]
        raise SystemExit(
            "Transition not found. Available transitions:\n"
            + json.dumps(available, indent=2, ensure_ascii=False)
        )

    payload = {"transition": {"id": selected.get("id")}}
    if not args.apply:
        print(
            json.dumps(
                {"mode": "dry-run", "action": "transition-status", "issueKey": issue_key, "selectedTransition": selected, "payload": payload},
                indent=2,
                ensure_ascii=False,
            )
        )
        return

    _, applied, _ = request_json("POST", jira_api_url(f"/rest/api/3/issue/{quote(issue_key)}/transitions"), payload)
    print(
        json.dumps(
            {"mode": "applied", "issueKey": issue_key, "selectedTransition": selected, "response": applied},
            indent=2,
            ensure_ascii=False,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="REST/CLI demo adapters for Jira Cloud")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate-connection-project", help="Validate Jira auth and project access")
    validate.set_defaults(func=lambda _args: validate_connection_project())

    create = subparsers.add_parser("create-demo-story", help="Create a demo story from an approved intent")
    create.add_argument("--intent", required=True, help="Path to approved intent.md")
    create.add_argument("--summary", help="Optional override for the Jira summary")
    create.add_argument("--apply", action="store_true", help="POST the story to Jira")
    create.set_defaults(func=create_demo_story)

    links = subparsers.add_parser("add-links", help="Add Git and Confluence remote links to a Jira issue")
    links.add_argument("--issue-key", required=True, help="Jira issue key")
    links.add_argument("--git-url", help="Git artifact URL or repository URL")
    links.add_argument("--git-title", help="Title for the Git remote link")
    links.add_argument("--confluence-url", help="Confluence page URL")
    links.add_argument("--confluence-title", help="Title for the Confluence remote link")
    links.add_argument("--apply", action="store_true", help="POST the remote links to Jira")
    links.set_defaults(func=add_links)

    transition = subparsers.add_parser("transition-status", help="Transition a Jira issue to a named transition or status")
    transition.add_argument("--issue-key", required=True, help="Jira issue key")
    transition.add_argument("--transition", help="Jira transition name")
    transition.add_argument("--to-status", help="Destination status name")
    transition.add_argument("--apply", action="store_true", help="POST the transition to Jira")
    transition.set_defaults(func=transition_status)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    env("JIRA_BASE_URL")
    env("JIRA_EMAIL")
    env("JIRA_API_TOKEN")
    env("JIRA_PROJECT_KEY")
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
