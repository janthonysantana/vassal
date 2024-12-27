import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()

def run_app():
    app = Flask(__name__)

    @app.get("/")
    def root():

        return {"status": "ready"}

    return app

# app = run_app()