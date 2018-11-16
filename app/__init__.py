"""Main Application Product Point."""

# third-party imports
from flask import Flask, jsonify

# local imports
from instance.config import app_config


def create_app(config_name):
    """Enables having instances of the
    application with different settings
    """

    # initializing the app
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    # app.config.from_object(configuration)


    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify(message='please try another page.', error='could not find requested data'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify(message='Sorry! Something went wrong. Try another time', error='SERVER DOWN'), 500

    return app