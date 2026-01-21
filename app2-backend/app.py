from flask import Flask, request, jsonify
import logging
import os

app = Flask(__name__)

# Configuration par variables d’environnement
APP_ENV = os.getenv("APP_ENV", "dev")

# Logs très verbeux (volontairement)
logging.basicConfig(level=logging.DEBUG)

@app.route("/api/data", methods=["GET"])
def get_data():
    user = request.args.get("user", "anonymous")
    app.logger.debug(f"Requête reçue de l'utilisateur : {user}")
    return jsonify({
        "message": f"Bonjour {user}",
        "environment": APP_ENV
    })

@app.route("/api/debug", methods=["POST"])
def debug():
    payload = request.get_json()
    app.logger.debug(f"Payload reçu : {payload}")
    return jsonify({
        "status": "received",
        "payload": payload
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
