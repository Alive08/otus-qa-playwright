#!/usr/bin/bash

/usr/bin/env python3 -m venv .venv
source .venv/bin/activate
pip install pip -U
pip install -r ./requirements.txt
playwright install
