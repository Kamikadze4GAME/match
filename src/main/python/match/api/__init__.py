from flask import Flask
from match.api.exceptions import (
    bad_request,
    page_not_found,
    method_not_allowed,
    server_error,
)
from match.api.routes import bp


def create_app():
    """Flask application/config factory"""
    app = Flask(__name__)
    app = register_error_handlers(app)
    app.register_blueprint(bp)
    return app


def register_error_handlers(app):
    app.errorhandler(400)(bad_request)
    app.errorhandler(404)(page_not_found)
    app.errorhandler(405)(method_not_allowed)
    app.errorhandler(500)(server_error)
    return app
