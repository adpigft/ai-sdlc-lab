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

    capability_path="$(awk -F': *' '/^[[:space:]]+path:/{print $2; exit}' "$state_file")"
    current_skill="$(awk -F': *' '/^[[:space:]]+current_skill:/{print $2; exit}' "$state_file")"

    if [[ -z "$capability_path" ]]; then
      error "$state_file" "capability.path is required"
    elif [[ ! -d "$capability_path" ]]; then
      error "$state_file" "capability.path does not exist: $capability_path"
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
  local state_file capability_path current_skill

  for state_file in "${workflow_states[@]}"; do
    capability_path="$(awk -F': *' '/^[[:space:]]+path:/{print $2; exit}' "$state_file")"
    current_skill="$(awk -F': *' '/^[[:space:]]+current_skill:/{print $2; exit}' "$state_file")"
    if [[ -n "$capability_path" && "$changed_file" == "$capability_path/"* ]]; then
      printf '%s\n' "$current_skill"
      return 0
    fi
  done

  printf '\n'
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
    intent|ba-intent|new)
      [[ "$changed_file" == */intent/* || "$changed_file" == */workflow-state.yaml ]]
      ;;
    specification|ba-specification)
      [[ "$changed_file" == */specs/* || "$changed_file" == */workflow-state.yaml ]]
      ;;
    architecture|architect-context)
      [[ "$changed_file" == */context/* || "$changed_file" == */contracts/* || "$changed_file" == */design/* || "$changed_file" == */workflow-state.yaml || "$changed_file" == decisions/* ]]
      ;;
    test-design|qa-test-design)
      [[ "$changed_file" == */tests/* || "$changed_file" == */workflow-state.yaml ]]
      ;;
    traceability-review)
      [[ "$changed_file" == */workflow-state.yaml || "$changed_file" == traceability/* ]]
      ;;
    implementation|developer-implementation)
      [[ "$changed_file" == */design/* || "$changed_file" == */workflow-state.yaml || "$changed_file" == src/* ]]
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
