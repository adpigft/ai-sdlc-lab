#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
output_dir="$repo_root/build/dashboard"
json_path="$output_dir/control-tower.json"
data_js_path="$output_dir/control-tower-data.js"

mkdir -p "$output_dir"

python3 "$repo_root/scripts/dashboard/generate-control-tower.py" --output "$json_path"

python3 - "$json_path" "$data_js_path" <<'PY'
from pathlib import Path
import json
import sys

json_path = Path(sys.argv[1])
data_js_path = Path(sys.argv[2])
payload = json.loads(json_path.read_text(encoding="utf-8"))
data_js_path.write_text("window.__CONTROL_TOWER_DATA__ = " + json.dumps(payload, indent=2, ensure_ascii=False) + ";\n", encoding="utf-8")
PY

printf '%s\n' "$repo_root/dashboard/control-tower.html"
printf '%s\n' "$json_path"
