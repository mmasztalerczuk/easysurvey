from flask import Blueprint, request

view = Blueprint('register', __name__)


@view.route("/register", methods=['POST'])
def register():
    """
    Create a new user
    ---
    security:
      - Bearer: []
    tags:
      - register
    parameters:
      - in: body
        name: body
        schema:
          $ref: '#/definitions/ResearchGroup'
        examples:
          one:
            name: "Research Group One"
    responses:
      201:
        description: Reserach Group created
      500:
        description: Internal Error
    """
    return ""

@view.route("/login", methods=['POST'])
def login():
    """
    Login
    ---
    security:
      - Bearer: []
    tags:
      - login
    parameters:
      - in: body
        name: body
        schema:
          $ref: '#/definitions/ResearchGroup'
        examples:
          one:
            name: "Research Group One"
    responses:
      201:
        description: Reserach Group created
      500:
        description: Internal Error
    """
    return ""
