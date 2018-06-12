from flask import Blueprint, request

view = Blueprint('notification', __name__)


@view.route("/notification", methods=['POST'])
def notification():
    """
    Send new notification
    ---
    security:
      - Bearer: []
    tags:
      - notification
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
