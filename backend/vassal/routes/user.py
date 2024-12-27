from flask import Blueprint, jsonify

from utils.logger import LOGGER

user_routes = Blueprint("user", __name__)

@user_routes.post("/user/register")
def register():
    LOGGER.info("Starting user registration...")
    return jsonify({"status": "registering"}), 201

@user_routes.post("/user/login")
def login():
    LOGGER.debug("Starting user login...")
    return jsonify({"status": "logging in"}), 200

@user_routes.post("/user/logout")
def logout():
    LOGGER.debug("Starting user logout...")
    return jsonify({"status": "logging in"}), 200