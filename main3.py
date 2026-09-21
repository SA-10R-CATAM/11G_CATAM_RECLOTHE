from flask import Flask, request, jsonify, send_from_directory
from pathlib import Path
from datetime import datetime

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent


@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "recreate.html")


@app.route("/sell", methods=["POST"])
def sell_clothes():

    data = request.get_json(silent=True) or {}

    required = [
        "name",
        "email",
        "clothing_type",
        "condition",
        "description",
        "price"
    ]

    if not all(data.get(field) for field in required):

        return jsonify({
            "message": "Please complete all required selling fields."
        }), 400


    print("\n--- NEW SELLING REQUEST ---")

    print(
        "Time:",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    print("Name:", data["name"])
    print("Email:", data["email"])
    print("Clothing:", data["clothing_type"])
    print("Condition:", data["condition"])
    print("Description:", data["description"])
    print("Expected price:", data["price"])

    print("---------------------------\n")


    return jsonify({
        "message":
        "Your clothing submission has been received! ReClothe by SPADZ will review it."
    })


@app.route("/buy", methods=["POST"])
def buy_clothes():

    data = request.get_json(silent=True) or {}

    required = [
        "name",
        "email",
        "clothing_type",
        "size",
        "budget",
        "condition"
    ]

    if not all(data.get(field) for field in required):

        return jsonify({
            "message": "Please complete all required buying fields."
        }), 400


    print("\n--- NEW BUYING REQUEST ---")

    print(
        "Time:",
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    print("Name:", data["name"])
    print("Email:", data["email"])
    print("Clothing:", data["clothing_type"])
    print("Size:", data["size"])
    print("Budget:", data["budget"])
    print("Condition:", data["condition"])
    print("Description:", data.get("description", ""))

    print("--------------------------\n")


    return jsonify({
        "message":
        "Your clothing request has been received! We will look for a matching ReClothe item."
    })


if __name__ == "__main__":

    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )