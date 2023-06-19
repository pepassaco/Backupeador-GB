#!/bin/bash
cd INSTALLATION_PATH/Backupeador-GB/
git pull origin main
#git submodule update --recursive --remote
source venv/bin/activate
python3 run.py