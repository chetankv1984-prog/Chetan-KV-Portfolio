from flask import Flask, render_template, request, jsonify
from pathlib import Path
from datetime import datetime, timezone
import sqlite3
import re

app = Flask(__name__)
DB = Path(__file__).with_name("messages.db")


def setup_db():
    with sqlite3.connect(DB) as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/api/contact")
def contact():
    data = request.get_json(silent=True) if request.is_json else request.form
    if not data:
        data = {}

    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip()
    message = str(data.get("message", "")).strip()

    valid_email = re.fullmatch(r"[^\s@]+@[^\s@]+\.[^\s@]+", email)
    if not (2 <= len(name) <= 100 and valid_email and 10 <= len(message) <= 3000):
        return jsonify(
            ok=False,
            error="Please enter a valid name, email and message (at least 10 characters)."
        ), 400

    with sqlite3.connect(DB) as con:
        con.execute(
            "INSERT INTO messages(name, email, message, created_at) VALUES (?, ?, ?, ?)",
            (name, email, message, datetime.now(timezone.utc).isoformat())
        )

    return jsonify(ok=True, message="Your message was saved. Thank you!")


setup_db()

if __name__ == "__main__":
    app.run(debug=True)
