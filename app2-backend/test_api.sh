#!/usr/bin/env bash
set -e

# Installer Flask dans l'environnement du runner
python3 -m pip install --upgrade pip
python3 -m pip install flask

# Lancer l'app backend
python3 app.py &
PID=$!

# Attendre que le serveur démarre
sleep 3

# Test de l'API
curl -s "http://127.0.0.1:5000/api/data?user=test" | grep -q "Bonjour test"

# Nettoyage
kill $PID
