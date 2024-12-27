
from dotenv import load_dotenv
from flask import Flask

from utils.logger import LOGGER
from routes.user import user_routes

load_dotenv()

def run_app():
    app = Flask(__name__)

    # Register routes
    app.register_blueprint(user_routes)

    @app.get("/")
    def root():

        return {"status": "ready"}

    return app

# app = run_app()