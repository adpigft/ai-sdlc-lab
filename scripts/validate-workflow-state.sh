#!/usr/bin/env bash
set -euo pipefail

failures=0

error() {
  local file="$1"
  local message="$2"
  echo "::error file=${file}::${message}"
  failures=1
}

workflow_states=()
while IFS= read -r file; do
  workflow_states+=("$file")
done < <(find domains -path '*/workflow-state.yaml' -type f | sort)

if [[ "${#workflow_states[@]}" -eq 0 ]]; then
  error "domains" "No workflow-state.yaml file found under domains/"
else
  for state_file in "${workflow_states[@]}"; do
    if [[ ! -s "$state_file" ]]; then
      error "$state_file" "workflow-state.yaml is empty"
      continue
    fi

    feature_path="$(awk '
      $0 == "feature:" { in_feature=1; next }
      /^[^[:space:]]/ { in_feature=0 }
      in_feature && $1 == "path:" {
        sub("^[[:space:]]*path:[[:space:]]*", "")
        gsub(/^"|"$/, "")
        print
        exit
      }
    ' "$state_file")"
    if [[ -z "$feature_path" ]]; then
      feature_path="$(awk -F': *' '/^[[:space:]]+path:/{print $2; exit}' "$state_file")"
    fi
    current_skill="$(awk -F': *' '/^[[:space:]]+current_skill:/{print $2; exit}' "$state_file")"

    if [[ -z "$feature_path" ]]; then
      error "$state_file" "feature.path is required"
    elif [[ ! -d "$feature_path" ]]; then
      error "$state_file" "feature.path does not exist: $feature_path"
    fi

    if [[ -z "$current_skill" ]]; then
      error "$state_file" "workflow.current_skill is required"
    fi

    echo "OK: $state_file"
  done
fi

changed_files=()
if [[ -n "${GITHUB_BASE_REF:-}" ]]; then
  git fetch --no-tags --depth=1 origin "$GITHUB_BASE_REF" >/dev/null 2>&1 || true
  while IFS= read -r file; do
    changed_files+=("$file")
  done < <(git diff --name-only "origin/${GITHUB_BASE_REF}...HEAD" 2>/dev/null || git diff --name-only HEAD~1...HEAD)
elif git rev-parse --verify HEAD >/dev/null 2>&1; then
  while IFS= read -r file; do
    changed_files+=("$file")
  done < <(git diff --name-only HEAD)
fi

if [[ "${#changed_files[@]}" -gt 0 ]]; then
  echo "Validating changed paths against workflow stage policy."
fi

current_skill_for_path() {
  local changed_file="$1"
  local state_file feature_path current_skill

  for state_file in "${workflow_states[@]}"; do
    feature_path="$(awk '
      $0 == "feature:" { in_feature=1; next }
      /^[^[:space:]]/ { in_feature=0 }
      in_feature && $1 == "path:" {
        sub("^[[:space:]]*path:[[:space:]]*", "")
        gsub(/^"|"$/, "")
        print
        exit
      }
    ' "$state_file")"
    if [[ -z "$feature_path" ]]; then
      feature_path="$(awk -F': *' '/^[[:space:]]+path:/{print $2; exit}' "$state_file")"
    fi
    current_skill="$(awk -F': *' '/^[[:space:]]+current_skill:/{print $2; exit}' "$state_file")"
    if [[ -n "$feature_path" && "$changed_file" == "$feature_path/"* ]]; then
      printf '%s\n' "$current_skill"
      return 0
    fi
  done

  printf '\n'
}

is_artifact_naming_migration_change() {
  local changed_file="$1"

  case "$changed_file" in
    domains/*/domain-context.md|\
    domains/*/README.md|\
    domains/*/capabilities/*/capability-context.md|\
    domains/*/capabilities/*/features/*/intent/intent.md|\
    domains/*/capabilities/*/features/*/specification/specification.md|\
    domains/*/capabilities/*/features/*/design/design.md|\
    domains/*/capabilities/*/features/*/contracts/openapi.yaml|\
    domains/*/capabilities/*/features/*/tests/acceptance.feature|\
    domains/*/capabilities/*/features/*/implementation/implementation-plan.md|\
    domains/*/capabilities/*/features/*/pr-review/pr-review-report.md|\
    domains/*/capabilities/*/features/*/validation/*.md|\
    domains/*/capabilities/*/features/*/release/*.md|\
    domains/*/capabilities/*/features/*/workflow-state.yaml|\
    domains/*/capabilities/*/intent/intent.md|\
    domains/*/capabilities/*/specification/specification.md|\
    domains/*/capabilities/*/specs/spec.md|\
    domains/*/capabilities/*/design/design.md|\
    domains/*/capabilities/*/context/context.md|\
    domains/*/capabilities/*/contracts/openapi.yaml|\
    domains/*/capabilities/*/tests/acceptance.feature|\
    domains/*/capabilities/*/implementation/implementation-plan.md|\
    domains/*/capabilities/*/design/implementation-plan.md|\
    domains/*/capabilities/*/validation/*.md|\
    domains/*/capabilities/*/release/*.md|\
    domains/*/capabilities/*/workflow-state.yaml)
      return 0
      ;;
    *)
      return 1
      ;;
  esac
}

is_allowed_for_skill() {
  local changed_file="$1"
  local current_skill="$2"

  case "$changed_file" in
    .github/workflows/*|scripts/*|framework/*|docs/automation/*|AGENTS.md|README.md)
      return 0
      ;;
    traceability/*)
      [[ "$current_skill" == "traceability-review" || "$current_skill" == "implementation" || "$current_skill" == "validation" || "$current_skill" == "release" ]]
      return
      ;;
    feedback/*)
      [[ "$current_skill" == "feedback-capture" || "$current_skill" == "release" ]]
      return
      ;;
    src/*)
      [[ "$current_skill" == "implementation" ]]
      return
      ;;
  esac

  case "$current_skill" in
    intent|ba-intent)
      [[ "$changed_file" == */intent/* || "$changed_file" == */workflow-state.yaml ]]
      ;;
    specification|ba-specification)
      [[ "$changed_file" == */specification/* || "$changed_file" == */specs/* || "$changed_file" == */workflow-state.yaml ]]
      ;;
    design|architect-context)
      [[ "$changed_file" == */design/* || "$changed_file" == */context/* || "$changed_file" == */contracts/* || "$changed_file" == */implementation/* || "$changed_file" == */workflow-state.yaml || "$changed_file" == decisions/* ]]
      ;;
    test-design|qa-test-design)
      [[ "$changed_file" == */tests/* || "$changed_file" == */workflow-state.yaml ]]
      ;;
    traceability-review)
      [[ "$changed_file" == */workflow-state.yaml || "$changed_file" == traceability/* ]]
      ;;
    implementation|developer-implementation)
      [[ "$changed_file" == */implementation/* || "$changed_file" == */design/* || "$changed_file" == */workflow-state.yaml || "$changed_file" == src/* ]]
      ;;
    pr-review)
      [[ "$changed_file" == */workflow-state.yaml ]]
      ;;
    validation|qa-validation)
      [[ "$changed_file" == */validation/* || "$changed_file" == */workflow-state.yaml ]]
      ;;
    release|devsecops-release)
      [[ "$changed_file" == */release/* || "$changed_file" == */workflow-state.yaml ]]
      ;;
    feedback-capture)
      [[ "$changed_file" == feedback/* || "$changed_file" == */workflow-state.yaml ]]
      ;;
    *)
      return 1
      ;;
  esac
}

if [[ "${#changed_files[@]}" -gt 0 ]]; then
  for changed_file in "${changed_files[@]}"; do
    [[ -z "$changed_file" ]] && continue

    case "$changed_file" in
      domains/*)
        if is_artifact_naming_migration_change "$changed_file"; then
          continue
        fi
        skill="$(current_skill_for_path "$changed_file")"
        if [[ -z "$skill" ]]; then
          error "$changed_file" "Domain artifact changed without a matching capability workflow-state.yaml"
        elif ! is_allowed_for_skill "$changed_file" "$skill"; then
          error "$changed_file" "Path change is not allowed while capability workflow current_skill is '$skill'"
        fi
        ;;
      traceability/*|feedback/*|src/*)
        active_skill="$(awk -F': *' '/^[[:space:]]+current_skill:/{print $2; exit}' "${workflow_states[0]:-/dev/null}" 2>/dev/null || true)"
        if ! is_allowed_for_skill "$changed_file" "$active_skill"; then
          error "$changed_file" "Path change is not allowed while active workflow current_skill is '${active_skill:-unknown}'"
        fi
        ;;
    esac
  done
fi

if [[ "$failures" -ne 0 ]]; then
  exit 1
fi

echo "Workflow state validation passed."
