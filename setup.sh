#!/bin/bash

python -m venv aienv
source aienv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload