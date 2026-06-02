#!/usr/bin/env bash
set -euo pipefail

failures=0

error() {
  local file="$1"
  local message="$2"
  echo "::error file=${file}::${message}"
  failures=1
}

contracts=()
while IFS= read -r file; do
  contracts+=("$file")
done < <(find domains -path '*/contracts/openapi.yaml' -type f | sort)

if [[ "${#contracts[@]}" -eq 0 ]]; then
  error "domains" "No OpenAPI contracts found under domains/"
fi

if ! command -v ruby >/dev/null 2>&1; then
  echo "::error::Ruby is required to parse YAML OpenAPI contracts"
  exit 1
fi

for contract in "${contracts[@]}"; do
  if [[ ! -s "$contract" ]]; then
    error "$contract" "OpenAPI contract is missing or empty"
    continue
  fi

  if ruby - "$contract" <<'RUBY'
require "yaml"

path = ARGV.fetch(0)
document = YAML.safe_load(File.read(path), aliases: true)

unless document.is_a?(Hash)
  warn "OpenAPI document must be a YAML mapping"
  exit 1
end

unless document.key?("openapi") || document.key?("swagger")
  warn "OpenAPI document must declare openapi or swagger"
  exit 1
end

unless document["paths"].is_a?(Hash)
  warn "OpenAPI document must declare a paths mapping"
  exit 1
end

unless document["info"].is_a?(Hash) && document["info"]["title"] && document["info"]["version"]
  warn "OpenAPI document must declare info.title and info.version"
  exit 1
end
RUBY
  then
    echo "OK: $contract"
  else
    error "$contract" "OpenAPI contract failed YAML/OpenAPI validation"
  fi
done

if [[ "$failures" -ne 0 ]]; then
  exit 1
fi

echo "OpenAPI validation passed."
