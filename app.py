import logging

from flask import Flask, jsonify
from flask_cors import CORS
from flask_swagger import swagger

from webapi.unit import view

logger = logging.getLogger(__name__)


def create_app():
    logger.info("Creating app")
    app = Flask(__name__)

    logger.info("Loading blueprints")
    app.register_blueprint(view)

    return app


def main():
    logger.info("Configuring MobiStats")
    app = create_app()
    logger.info("Starting MobiStats")

    return app


app = main()
CORS(app)


@app.route("/spec")
def spec():
    swag = swagger(app)


    swag['securityDefinitions'] = {
        "Bearer": {
            "in": "header",
            "type": "apiKey",
            "name": "Authorization"
            }
        }


    return jsonify(swag)