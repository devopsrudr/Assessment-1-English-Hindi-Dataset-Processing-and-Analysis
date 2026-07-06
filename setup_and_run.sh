#!/bin/bash
# One-click setup + run for Assignment 2 (translation + BLEU/CHRF/TER scoring).
# Usage:  bash setup_and_run.sh

set -e
cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

echo "Installing dependencies (this can take a few minutes the first time,"
echo "torch + transformers are large downloads)..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

echo ""
echo "Running translation + evaluation script..."
echo "(The first run will also download the MT model itself from Hugging Face,"
echo " a few hundred MB — needs internet access.)"
echo ""
python3 translate_and_evaluate.py "$@"
