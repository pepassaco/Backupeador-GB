#!/bin/bash
cd "$(cd "$(dirname "$0")" && pwd)/.."
git pull origin main
#git submodule update --recursive --remote
source venv/bin/activate
python3 run.py