from flask import Flask,make_response,request
from drugstore.views import comm_bp


def create_app():
    app=Flask(__name__)
    register_blueprints(app)
    return app

def register_blueprints(app):
    app.register_blueprint(comm_bp)

