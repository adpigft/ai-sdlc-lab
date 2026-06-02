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

pending_artifact_path() {
  local file="$1"
  awk '
    /^pending_gate:/ { in_section=1; next }
    /^[^[:space:]]/ { in_section=0 }
    in_section && $1 == "artifact_path:" {
      sub("^[[:space:]]*artifact_path:[[:space:]]*", "")
      gsub(/^"|"$/, "")
      print
      exit
    }
  ' "$file"
}

is_partial_non_production_release() {
  local file="$1"
  grep -Eiq 'partial[ -]?(non[ -]?production|pilot|lab|internal)[ -]?release|non[ -]?production release|pilot release|lab release|internal release' "$file"
}

workflow_states=()
while IFS= read -r file; do
  workflow_states+=("$file")
done < <(find domains -path '*/workflow-state.yaml' -type f | sort)

if [[ "${#workflow_states[@]}" -eq 0 ]]; then
  error "domains" "No workflow-state.yaml file found under domains/"
fi

for state_file in "${workflow_states[@]}"; do
  current_state="$(field_value workflow current_state "$state_file")"
  validation_report="$(field_value artifacts validation_report "$state_file")"
  release_notes="$(field_value artifacts release_notes "$state_file")"
  pending_release_notes="$(pending_artifact_path "$state_file")"

  if [[ -n "$release_notes" && ! -s "$release_notes" ]]; then
    error "$release_notes" "release_notes is declared in workflow-state.yaml but the file is missing or empty"
  fi

  case "$current_state" in
    release_ready|released)
      if [[ -z "$validation_report" || ! -s "$validation_report" ]]; then
        error "$state_file" "current_state is '$current_state' but validation_report is missing or empty"
        continue
      fi

      if [[ -z "$release_notes" ]]; then
        if [[ -n "$pending_release_notes" ]]; then
          error "$state_file" "current_state is '$current_state' but artifacts.release_notes is empty; expected non-empty release notes at '$pending_release_notes'"
        else
          error "$state_file" "current_state is '$current_state' but artifacts.release_notes is empty"
        fi
      elif [[ ! -s "$release_notes" ]]; then
        error "$release_notes" "current_state is '$current_state' but release notes are missing or empty"
      fi

      if grep -Eiq 'release[[:space:]-]*not[[:space:]-]*ready|not[[:space:]-]*ready[[:space:]-]*for[[:space:]-]*release' "$validation_report"; then
        error "$validation_report" "workflow current_state is '$current_state' but validation report says release is not ready"
      fi

      if grep -Eiq 'partial validation|partial[[:space:]-]*validation[[:space:]-]*complete' "$validation_report" && ! is_partial_non_production_release "$validation_report"; then
        error "$validation_report" "workflow current_state is '$current_state' but validation report says validation is partial and is not marked as a partial/non-production release"
      fi

      if grep -Eiq 'remaining .*not validated|not yet validated|remaining slices.*not implemented|downstream .*missing|remaining slices are not validated' "$validation_report" && ! is_partial_non_production_release "$validation_report"; then
        error "$validation_report" "workflow current_state is '$current_state' but validation report indicates remaining validation/slices are incomplete without a partial/non-production release marker"
      fi
      ;;
  esac
done

if [[ "$failures" -ne 0 ]]; then
  exit 1
fi

echo "Release readiness validation passed."
