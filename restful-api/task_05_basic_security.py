#!/usr/bin/python3
"""
API Security and Authentication module using Flask,
Flask-HTTPAuth, and Flask-JWT-Extended.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key-change-in-production"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Auth."""
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Protected route requiring Basic HTTP Authentication."""
    return "Basic Auth: Access Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing authorization header/token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle malformed or signature-mismatched token."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Handle expired token error."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Handle revoked token error."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """Handle non-fresh token error."""
    return jsonify({"error": "Fresh token required"}), 401


@app.route("/login", methods=["POST"])
def login():
    """Authenticates credentials and returns a JWT access token."""
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protected route requiring a valid JWT Token."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Protected route requiring JWT token with 'admin' role."""
    current_username = get_jwt_identity()
    user = users.get(current_username)

    if not user or user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()