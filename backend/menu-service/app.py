"""
app.py — menu-service
A small Flask microservice that owns the restaurant menu. It is the only
service allowed to read and write the menu_items table. Other services,
such as order-service, communicate with this service through its API.
"""
from flask import Flask, jsonify
from flask_cors import CORS
from psycopg2 import OperationalError
from db import get_connection

app = Flask(__name__)

# Allow the frontend (different origin/port) to call this API.
CORS(app)


@app.route("/health", methods=["GET"])
def health():
    """Used by Docker, Jenkins, and Kubernetes to check the service."""
    return jsonify({
        "status": "ok",
        "service": "menu-service"
    })


@app.route("/api/menu", methods=["GET"])
def get_menu():
    try:
        conn = get_connection()
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                SELECT
                    id,
                    category,
                    name,
                    description AS desc,
                    price,
                    heat
                FROM menu_items
                ORDER BY category, price
                """
            )
            rows = cur.fetchall()
        conn.close()

        # Convert every database row into a JSON-friendly menu item.
        menu = [
            {
                "id": row["id"],
                "category": row["category"],
                "name": row["name"],
                "desc": row["desc"],
                "price": float(row["price"]),
                "heat": row["heat"],
            }
            for row in rows
        ]
        return jsonify(menu)
    except OperationalError as err:
        return jsonify({
            "error": "database unavailable",
            "detail": str(err)
        }), 503


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
