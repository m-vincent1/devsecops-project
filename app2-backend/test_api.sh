#!/usr/bin/env bash
set -e

python -m venv .venv
source .venv/bin/activate
pip install -q flask

python app.py &
PID=$!
sleep 2

curl -s "http://127.0.0.1:5000/api/data?user=test" | grep -q "Bonjour test"

kill $PID
