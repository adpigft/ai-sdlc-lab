#!/usr/bin/env python3
"""GitHub Actions evidence adapter using the `gh` CLI.

This script reads workflow runs and the latest validation result for the
configured repository. It does not mutate GitHub state.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from typing import Any


def env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise SystemExit(f"Missing required environment variable: {name}")
    return value


def repo_spec() -> str:
    return f"{env('GITHUB_OWNER')}/{env('GITHUB_REPO')}"


def gh_env() -> dict[str, str]:
    environment = os.environ.copy()
    token = environment.get("GITHUB_TOKEN", "").strip() or environment.get("GH_TOKEN", "").strip()
    if token:
        environment["GH_TOKEN"] = token
    return environment


def run_gh(args: list[str]) -> Any:
    completed = subprocess.run(
        ["gh", *args],
        check=False,
        capture_output=True,
        text=True,
        env=gh_env(),
    )
    if completed.returncode != 0:
        raise SystemExit(
            "gh command failed:\n"
            + " ".join(["gh", *args])
            + "\n"
            + completed.stderr.strip()
        )
    output = completed.stdout.strip()
    return json.loads(output) if output else None


def list_latest_workflow_runs(limit: int) -> None:
    runs = run_gh(
        [
            "run",
            "list",
            "-R",
            repo_spec(),
            "-L",
            str(limit),
            "--json",
            "attempt,conclusion,createdAt,databaseId,displayTitle,event,headBranch,headSha,name,number,startedAt,status,updatedAt,url,workflowDatabaseId,workflowName",
        ]
    )
    print(json.dumps({"repository": repo_spec(), "runs": runs or []}, indent=2, ensure_ascii=False))


def latest_validation_result(limit: int, workflow_name: str) -> None:
    runs = run_gh(
        [
            "run",
            "list",
            "-R",
            repo_spec(),
            "-L",
            str(limit),
            "--workflow",
            workflow_name,
            "--json",
            "attempt,conclusion,createdAt,databaseId,displayTitle,event,headBranch,headSha,name,number,startedAt,status,updatedAt,url,workflowDatabaseId,workflowName",
        ]
    ) or []

    if not runs:
        runs = run_gh(
            [
                "run",
                "list",
                "-R",
                repo_spec(),
                "-L",
                "1",
                "--json",
                "attempt,conclusion,createdAt,databaseId,displayTitle,event,headBranch,headSha,name,number,startedAt,status,updatedAt,url,workflowDatabaseId,workflowName",
            ]
        ) or []

    if not runs:
        print(json.dumps({"repository": repo_spec(), "workflow": workflow_name, "result": "no-runs-found"}, indent=2, ensure_ascii=False))
        return

    latest_run = runs[0]
    run_id = latest_run.get("databaseId")
    run_view = run_gh(
        [
            "run",
            "view",
            "-R",
            repo_spec(),
            str(run_id),
            "--json",
            "attempt,conclusion,createdAt,databaseId,displayTitle,event,headBranch,headSha,jobs,name,number,startedAt,status,updatedAt,url,workflowDatabaseId,workflowName",
        ]
    )

    print(
        json.dumps(
            {
                "repository": repo_spec(),
                "workflow": workflow_name,
                "latestRun": latest_run,
                "latestValidationResult": run_view,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="GitHub Actions evidence adapter using gh")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_runs = subparsers.add_parser("list-latest-workflow-runs", help="List the latest workflow runs")
    list_runs.add_argument("--limit", type=int, default=10, help="Maximum number of runs to fetch")
    list_runs.set_defaults(func=lambda args: list_latest_workflow_runs(args.limit))

    latest = subparsers.add_parser("latest-validation-result", help="Fetch the latest validation workflow result")
    latest.add_argument("--workflow", default="AI SDLC Validation", help="Workflow name to inspect")
    latest.add_argument("--limit", type=int, default=10, help="Maximum number of runs to search")
    latest.set_defaults(func=lambda args: latest_validation_result(args.limit, args.workflow))

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    env("GITHUB_OWNER")
    env("GITHUB_REPO")
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
