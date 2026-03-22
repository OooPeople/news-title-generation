#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 2 ]; then
    echo "Usage: bash scripts/run_inference.sh <input_jsonl> <output_jsonl>"
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

python "${REPO_ROOT}/src/run_mt5.py" \
    --do_predict \
    --model_name_or_path "${REPO_ROOT}/mt5-small" \
    --test_file "${1}" \
    --output_dir "${REPO_ROOT}/mt5-predict_beam5" \
    --output_file "${2}" \
    --predict_with_generate \
    --text_column maintext \
    --summary_column title \
    --per_device_eval_batch_size 4 \
    --num_beams 5
