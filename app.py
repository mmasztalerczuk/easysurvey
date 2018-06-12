import logging

from flask import Flask, jsonify
from flask_cors import CORS
from flask_swagger import swagger

from webapi.unit import view
from webapi.research_group import view as view2
from webapi.survay import view as view4
from webapi.question import view as view5
from webapi.register import view as view6
from webapi.participant.research_group import view as view3

logger = logging.getLogger(__name__)


def create_app():
    logger.info("Creating app")
    app = Flask(__name__)

    logger.info("Loading blueprints")
    app.register_blueprint(view)
    app.register_blueprint(view2)
    app.register_blueprint(view3)
    app.register_blueprint(view4)
    app.register_blueprint(view5)
    app.register_blueprint(view6)

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
            },
        "Participant": {
            "in": "header",
            "type": "apiKey",
            "name": "DeviceId"
            }
        }


    return jsonify(swag)