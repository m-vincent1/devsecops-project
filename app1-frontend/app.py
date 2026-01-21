from flask import Flask, request
import requests
import logging
import os

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

# En local : on pointe vers localhost
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:5000")

@app.route("/")
def index():
    user = request.args.get("user", "anonymous")
    r = requests.get(f"{BACKEND_URL}/api/data", params={"user": user}, timeout=3)
    return r.text, r.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
