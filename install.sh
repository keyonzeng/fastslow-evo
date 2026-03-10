#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
python3 "$DIR/scripts/install_openclaw.py"
python3 "$DIR/scripts/setup_runtime.py"
