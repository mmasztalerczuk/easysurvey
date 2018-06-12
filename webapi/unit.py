from flask import Blueprint, request

view = Blueprint('view', __name__)


@view.route("/unit", methods=['POST'])
def unit():
    """
    Create a new Unit
    ---
    security:
      - Bearer: []
    tags:
      - unit
    parameters:
      - in: body
        name: body
        schema:
          $ref: '#/definitions/Unit'
        examples:
          one:
            name: "Unit One"
    responses:
      201:
        description: Unit created
      500:
        description: Internal Error
    """
    return


@view.route("/unit", methods=['GET'])
def get_unit():
    """
    Get all unit
    ---
    definitions:
      - schema:
          id: Unit
          properties:
            id:
              type: integer
              description: id of unit
              readOnly: true
            name:
              type: string
              description: name of the unit
              example: My new unit
    security:
      - Bearer: []
    tags:
      - unit
    responses:
      200:
        description: Get all units of user
        schema:
          type: array
          items:
            $ref: '#/definitions/Unit'
          example:
            - id: 0
              name: Unit One
            - id: 1
              name: Unit Two
    """

    return ""
