#!/usr/bin/env python3
"""REST/CLI demo adapters for Confluence Cloud.

This script validates Confluence access, publishes reviewed Git artifacts, and
updates pages by title. It uses environment variables only and does not write
unless `--apply` is supplied.
"""

from __future__ import annotations

import argparse
import base64
import html
import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
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


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def relative_path(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def jira_base_url() -> str:
    return env("JIRA_BASE_URL").rstrip("/")


def confluence_base_url() -> str:
    override = optional_env("CONFLUENCE_BASE_URL")
    if override:
        return override.rstrip("/")
    return f"{jira_base_url()}/wiki"


def confluence_api_url(path: str) -> str:
    return f"{confluence_base_url()}{path}"


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


def validate_space() -> dict[str, Any]:
    space_key = env("CONFLUENCE_SPACE_KEY")
    _, response, _ = request_json("GET", confluence_api_url(f"/rest/api/space/{quote(space_key)}"))
    if not isinstance(response, dict):
        raise SystemExit("Unexpected Confluence space response")
    result = {
        "spaceKey": response.get("key", space_key),
        "spaceId": response.get("id"),
        "name": response.get("name"),
        "baseUrl": confluence_base_url(),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return result


def load_source(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"Source artifact not found: {path}")
    return read_text(path)


def build_storage_body(title: str, source_path: Path, source_text: str) -> str:
    escaped_title = html.escape(title)
    escaped_source = html.escape(relative_path(source_path))
    escaped_text = html.escape(source_text)
    return "\n".join(
        [
            f"<h1>{escaped_title}</h1>",
            "<p><strong>Published View Only:</strong> Git remains the source of truth. This page is generated from Git artifacts for stakeholder review.</p>",
            "<table><tbody>",
            f"<tr><th>Source Artifact</th><td>{escaped_source}</td></tr>",
            f"<tr><th>Space Key</th><td>{html.escape(env('CONFLUENCE_SPACE_KEY'))}</td></tr>",
            "</tbody></table>",
            "<h2>Source Content</h2>",
            f"<pre>{escaped_text}</pre>",
        ]
    )


def find_page_by_title(space_id: str, title: str) -> dict[str, Any] | None:
    query = urlencode({"space-id": space_id, "title": title, "limit": "10", "body-format": "storage"})
    _, response, _ = request_json("GET", confluence_api_url(f"/api/v2/pages?{query}"))
    if not isinstance(response, dict):
        return None
    results = response.get("results", [])
    exact_matches = [page for page in results if clean(page.get("title")) == clean(title)]
    if len(exact_matches) == 1:
        return exact_matches[0]
    if len(exact_matches) > 1:
        raise SystemExit(f"More than one Confluence page matched title: {title}")
    return None


def create_page_payload(space_id: str, title: str, body: str, parent_id: str | None = None) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "spaceId": space_id,
        "status": "current",
        "title": title,
        "body": {"representation": "storage", "value": body},
    }
    if parent_id:
        payload["parentId"] = parent_id
    return payload


def update_page_payload(page: dict[str, Any], title: str, body: str) -> dict[str, Any]:
    version = int((page.get("version") or {}).get("number", 0)) + 1
    payload: dict[str, Any] = {
        "id": page.get("id"),
        "status": "current",
        "title": title,
        "body": {"representation": "storage", "value": body},
        "version": {"number": version, "message": "Updated by REST/CLI demo adapter"},
    }
    if page.get("parentId"):
        payload["parentId"] = page["parentId"]
    return payload


def publish_page(args: argparse.Namespace) -> None:
    space = validate_space()
    source_path = Path(args.source).expanduser().resolve()
    source_text = load_source(source_path)
    title = clean(args.title) or source_path.stem.replace("-", " ").title()
    body = build_storage_body(title, source_path, source_text)
    payload = create_page_payload(str(space["spaceId"]), title, body, args.parent_id)

    if not args.apply:
        print(json.dumps({"mode": "dry-run", "action": "publish-approved-git-artifact-page", "payload": payload}, indent=2, ensure_ascii=False))
        return

    _, response, _ = request_json("POST", confluence_api_url("/api/v2/pages"), payload)
    print(
        json.dumps(
            {
                "mode": "applied",
                "spaceKey": space["spaceKey"],
                "pageId": response.get("id") if isinstance(response, dict) else None,
                "title": response.get("title") if isinstance(response, dict) else title,
                "url": response.get("_links", {}).get("webui") if isinstance(response, dict) else None,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


def update_page(args: argparse.Namespace) -> None:
    space = validate_space()
    source_path = Path(args.source).expanduser().resolve()
    source_text = load_source(source_path)
    title = clean(args.title)
    if not title:
        raise SystemExit("--title is required")
    body = build_storage_body(title, source_path, source_text)
    page = find_page_by_title(str(space["spaceId"]), title)
    if page is None:
        raise SystemExit(f"No Confluence page found with title: {title}")

    payload = update_page_payload(page, title, body)
    if not args.apply:
        print(json.dumps({"mode": "dry-run", "action": "update-page-by-title", "page": page, "payload": payload}, indent=2, ensure_ascii=False))
        return

    _, response, _ = request_json("PUT", confluence_api_url(f"/api/v2/pages/{quote(str(page['id']))}"), payload)
    print(
        json.dumps(
            {
                "mode": "applied",
                "spaceKey": space["spaceKey"],
                "pageId": response.get("id") if isinstance(response, dict) else page.get("id"),
                "title": response.get("title") if isinstance(response, dict) else title,
                "url": response.get("_links", {}).get("webui") if isinstance(response, dict) else None,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="REST/CLI demo adapters for Confluence Cloud")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate-space", help="Validate Confluence access and space availability")
    validate.set_defaults(func=lambda _args: validate_space())

    publish = subparsers.add_parser("publish-approved-git-artifact-page", help="Create a new Confluence page from an approved Git artifact")
    publish.add_argument("--source", required=True, help="Path to the Git artifact or generated summary")
    publish.add_argument("--title", help="Optional page title override")
    publish.add_argument("--parent-id", help="Optional parent page id")
    publish.add_argument("--apply", action="store_true", help="POST the page to Confluence")
    publish.set_defaults(func=publish_page)

    update = subparsers.add_parser("update-page-by-title", help="Update an existing Confluence page by title")
    update.add_argument("--source", required=True, help="Path to the Git artifact or generated summary")
    update.add_argument("--title", required=True, help="Exact page title to update")
    update.add_argument("--apply", action="store_true", help="PUT the updated page to Confluence")
    update.set_defaults(func=update_page)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    env("JIRA_BASE_URL")
    env("JIRA_EMAIL")
    env("JIRA_API_TOKEN")
    env("CONFLUENCE_SPACE_KEY")
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
