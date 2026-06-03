#!/usr/bin/env bash
set -euo pipefail

failures=0

error() {
  local file="$1"
  local message="$2"
  echo "::error file=${file}::${message}"
  failures=1
}

required_global_files=(
  "traceability/traceability-matrix.md"
  "feedback/feedback-log.md"
)

for file in "${required_global_files[@]}"; do
  if [[ ! -s "$file" ]]; then
    error "$file" "Required repository artifact is missing or empty"
  else
    echo "OK: $file"
  fi
done

workflow_states=()
while IFS= read -r file; do
  workflow_states+=("$file")
done < <(find domains -path '*/workflow-state.yaml' -type f | sort)

if [[ "${#workflow_states[@]}" -eq 0 ]]; then
  error "domains" "No workflow-state.yaml file found under domains/"
fi

required_keys_for_skill() {
  case "$1" in
    intent|ba-intent)
      printf '%s\n' intent
      ;;
    specification|ba-specification)
      printf '%s\n' intent specification
      ;;
    design|architect-context)
      printf '%s\n' intent specification architecture api_contract
      ;;
    test-design|qa-test-design)
      printf '%s\n' intent specification architecture api_contract test_design
      ;;
    traceability-review)
      printf '%s\n' intent specification architecture api_contract test_design traceability
      ;;
    implementation|developer-implementation)
      printf '%s\n' intent specification architecture api_contract test_design implementation_plan traceability
      ;;
    pr-review)
      printf '%s\n' intent specification architecture api_contract test_design implementation_plan traceability
      ;;
    validation|qa-validation)
      printf '%s\n' intent specification architecture api_contract test_design implementation_plan validation_report traceability
      ;;
    release|devsecops-release|feedback-capture)
      printf '%s\n' intent specification architecture api_contract test_design implementation_plan validation_report traceability
      ;;
    *)
      printf '%s\n' intent specification architecture api_contract test_design traceability
      ;;
  esac
}

artifact_value() {
  local key="$1"
  local state_file="$2"
  awk -v key="$key" '
    /^artifacts:/ { in_artifacts=1; next }
    /^[^[:space:]]/ { in_artifacts=0 }
    in_artifacts && $1 == key ":" {
      sub("^[[:space:]]*" key ":[[:space:]]*", "")
      gsub(/^"|"$/, "")
      print
      exit
    }
  ' "$state_file"
}

for state_file in "${workflow_states[@]}"; do
  current_skill="$(awk -F': *' '/^[[:space:]]+current_skill:/{print $2; exit}' "$state_file")"
  [[ -z "$current_skill" ]] && current_skill="unknown"

  while IFS= read -r key; do
    [[ -z "$key" ]] && continue
    value="$(artifact_value "$key" "$state_file")"

    if [[ -z "$value" ]]; then
      error "$state_file" "Required artifact key '$key' is missing for current_skill '$current_skill'"
    elif [[ ! -s "$value" ]]; then
      error "$value" "Required artifact '$key' is missing or empty"
    else
      echo "OK: $key -> $value"
    fi
  done < <(required_keys_for_skill "$current_skill")
done

if [[ "$failures" -ne 0 ]]; then
  exit 1
fi

echo "Artifact validation passed."
