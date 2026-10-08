#!/usr/bin/python3
"""
Simple API implementation using Flask.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)


users = {}


@app.route("/")
def home():
    """Root endpoint returning a welcome message."""
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """Returns a JSON list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Status endpoint returning OK."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Returns the user object corresponding to the given username.
    Returns 404 if the user is not found.
    """
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the users dictionary via POST request.
    Handles validation for JSON formatting, missing username, and duplicates.
    """
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")

    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
