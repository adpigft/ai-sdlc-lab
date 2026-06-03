#!/usr/bin/env bash
set -euo pipefail

failures=0

error() {
  local file="$1"
  local message="$2"
  echo "::error file=${file}::${message}"
  failures=1
}

field_value() {
  local section="$1"
  local key="$2"
  local file="$3"
  awk -v section="$section" -v key="$key" '
    $0 == section ":" { in_section=1; next }
    /^[^[:space:]]/ { in_section=0 }
    in_section && $1 == key ":" {
      sub("^[[:space:]]*" key ":[[:space:]]*", "")
      gsub(/^"|"$/, "")
      print
      exit
    }
  ' "$file"
}

check_artifact_paths() {
  local state_file="$1"
  awk '
    /^artifacts:/ { in_artifacts=1; next }
    /^[^[:space:]]/ { in_artifacts=0 }
    in_artifacts && /^[[:space:]]+[A-Za-z0-9_]+:/ {
      key=$1
      sub(":", "", key)
      value=$0
      sub("^[[:space:]]*" key ":[[:space:]]*", "", value)
      gsub(/^"|"$/, "", value)
      if (value != "") {
        print key "|" value
      }
    }
  ' "$state_file"
}

expected_next_skill() {
  case "$1" in
    intent_review) printf '%s\n' specification ;;
    specification_review) printf '%s\n' design ;;
    design_review) printf '%s\n' test-design ;;
    test_review) printf '%s\n' implementation ;;
    implementation_ready) printf '%s\n' implementation ;;
    implementation_in_progress) printf '%s\n' pr-review ;;
    pr_review_ready) printf '%s\n' validation ;;
    validation_ready) printf '%s\n' release ;;
    release_ready) printf '%s\n' feedback-capture ;;
    released) printf '%s\n' feedback-capture ;;
    blocked) printf '%s\n' "" ;;
    *) printf '%s\n' "" ;;
  esac
}

workflow_states=()
while IFS= read -r file; do
  workflow_states+=("$file")
done < <(find domains -path '*/workflow-state.yaml' -type f | sort)

if [[ "${#workflow_states[@]}" -eq 0 ]]; then
  error "domains" "No workflow-state.yaml file found under domains/"
fi

traceability_file="traceability/traceability-matrix.md"
if [[ ! -s "$traceability_file" ]]; then
  error "$traceability_file" "Traceability matrix is missing or empty"
fi

for state_file in "${workflow_states[@]}"; do
  capability_id="$(field_value capability capability_id "$state_file")"
  capability_name="$(field_value capability name "$state_file")"
  current_state="$(field_value workflow current_state "$state_file")"
  current_skill="$(field_value workflow current_skill "$state_file")"
  next_skill="$(field_value workflow next_skill "$state_file")"
  current_artifact_path="$(field_value current_artifact path "$state_file")"
  validation_report="$(field_value artifacts validation_report "$state_file")"
  release_notes="$(field_value artifacts release_notes "$state_file")"

  if [[ -z "$current_state" ]]; then
    error "$state_file" "workflow.current_state is required"
  fi

  if [[ -z "$current_skill" ]]; then
    error "$state_file" "workflow.current_skill is required"
  fi

  expected="$(expected_next_skill "$current_state")"
  if [[ -n "$expected" && "$next_skill" != "$expected" ]]; then
    error "$state_file" "workflow.next_skill is '$next_skill' but expected '$expected' for current_state '$current_state'"
  fi

  if [[ -n "$current_artifact_path" && ! -s "$current_artifact_path" ]]; then
    error "$current_artifact_path" "current_artifact.path is populated but the file is missing or empty"
  fi

  while IFS="|" read -r key path; do
    [[ -z "$key" || -z "$path" ]] && continue
    if [[ ! -s "$path" ]]; then
      error "$path" "artifacts.$key is declared in workflow-state.yaml but the file is missing or empty"
    fi
  done < <(check_artifact_paths "$state_file")

  case "$current_state" in
    validation_ready|release_ready|released)
      if [[ -z "$validation_report" || ! -s "$validation_report" ]]; then
        error "$state_file" "current_state '$current_state' requires a non-empty artifacts.validation_report"
      fi
      ;;
  esac

  case "$current_state" in
    release_ready|released)
      if [[ -z "$release_notes" || ! -s "$release_notes" ]]; then
        error "$state_file" "current_state '$current_state' requires a non-empty artifacts.release_notes"
      fi
      if [[ -n "$validation_report" && -s "$validation_report" ]] && grep -Eiq 'release[[:space:]-]*not[[:space:]-]*ready|not[[:space:]-]*ready[[:space:]-]*for[[:space:]-]*release' "$validation_report"; then
        error "$validation_report" "current_state '$current_state' conflicts with validation report release readiness text"
      fi
      ;;
  esac

  if [[ "$current_state" == "released" && -z "$release_notes" ]]; then
    error "$state_file" "released workflow must declare artifacts.release_notes"
  fi

  if [[ -s "$traceability_file" ]]; then
    if [[ -n "$capability_id" ]] && ! grep -qi "$capability_id" "$traceability_file"; then
      error "$traceability_file" "Traceability matrix does not mention active capability id '$capability_id'"
    elif [[ -z "$capability_id" && -n "$capability_name" ]] && ! grep -qi "$capability_name" "$traceability_file"; then
      error "$traceability_file" "Traceability matrix does not mention active capability '$capability_name'"
    fi
  fi
done

if [[ "$failures" -ne 0 ]]; then
  exit 1
fi

echo "Workflow consistency validation passed."
