#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m ipykernel install --user \
  --name e7ai-session0-1 \
  --display-name "Python (E7AI session0-1)"
