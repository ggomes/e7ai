#!/usr/bin/env bash
python -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 -m ipykernel install --user \
  --name e7ai-session0-1 \
  --display-name "Python (E7AI session0-1)"
