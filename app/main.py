from flask import Flask, request, jsonify
from datetime import datetime

from app.db import insert_log
from app.schema import init_db

app = Flask(__name__)

init_db()


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "AI Focus Monitor Running"
    })


@app.route("/log", methods=["POST"])
def log_activity():

    try:
        data = request.json

        timestamp = datetime.now().isoformat()

        app_name = data.get("app_name", "unknown")
        window_title = data.get("window_title", "unknown")
        status = data.get("status", "Coding")
        idle_seconds = data.get("idle_seconds", 0)

        insert_log(
            timestamp,
            app_name,
            window_title,
            status,
            idle_seconds
        )

        return jsonify({"status": "success"})

    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )