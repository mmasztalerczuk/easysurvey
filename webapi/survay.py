from flask import Blueprint, request

view = Blueprint('survey', __name__)


@view.route("/survey", methods=['POST'])
def survey():
    """
    Create a new survey
    ---
    security:
      - Bearer: []
    tags:
      - survey
    parameters:
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Survey'
        examples:
          one:
            name: "Survey 1"
    responses:
      201:
        description: Survey created
      500:
        description: Internal Error
    """
    return ""


@view.route("/survey", methods=['GET'])
def get_survies():
    """
    Get all survey for given research group
    ---
    definitions:
      - schema:
          id: Survey
          properties:
            name:
              type: string
              description: name of the survey group
              example: My new survey
    security:
      - Bearer: []
    tags:
      - survey
    responses:
      200:
        description: Get all survey
        schema:
          type: array
          items:
            $ref: '#/definitions/Survey'
          example:
            - name: Research Group One
            - name: Research Group Two
    """

    return ""
