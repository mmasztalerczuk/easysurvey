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
          id: Unit
          required:
            - name
          properties:
            name:
              type: string
              description: name for unit
    responses:
      201:
        description: Unit created
    """
    return


@view.route("/unit", methods=['GET'])
def get_unit():
    """
    Get all unit
    ---
    security:
      - Bearer: []
    tags:
      - unit
    responses:
      200:
        description: Unit created
    """
    print(request.headers)
    return ""
