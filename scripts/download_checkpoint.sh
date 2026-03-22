#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

cd "${REPO_ROOT}"
wget https://www.dropbox.com/s/v7k2hvbkvst60m7/mt5-small.zip?dl=1 -O mt5-small.zip
unzip -o mt5-small.zip
