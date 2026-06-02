#!/usr/bin/env bash
set -euo pipefail

traceability_file="traceability/traceability-matrix.md"

if [[ ! -s "$traceability_file" ]]; then
  echo "::error file=${traceability_file}::Traceability matrix is missing or empty"
  exit 1
fi

required_terms=(
  "Intent"
  "Requirement"
  "Architecture"
  "Test"
  "Validation"
)

for term in "${required_terms[@]}"; do
  if ! grep -qi "$term" "$traceability_file"; then
    echo "::error file=${traceability_file}::Traceability matrix does not reference '$term'"
    exit 1
  fi
done

echo "Traceability validation passed."
