from flask import Blueprint, request

view = Blueprint('view2', __name__)


@view.route("/research_group", methods=['POST'])
def research_group():
    """
    Create a new Research Group
    ---
    security:
      - Bearer: []
    tags:
      - research_group
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


@view.route("/research_group", methods=['GET'])
def get_research_group():
    """
    Get all research group for given id of unit
    ---
    definitions:
      - schema:
          id: ResearchGroup
          properties:
            id:
              type: integer
              description: uniq id of research group
              readOnly: true
            name:
              type: string
              description: name of the research group
              example: My new research group
            unit_id:
              type: string
              description: id of unit where research group will be added
              example: 0
    security:
      - Bearer: []
    tags:
      - research_group
    responses:
      200:
        description: Get all research groups of user
        schema:
          type: array
          items:
            $ref: '#/definitions/ResearchGroup'
          example:
            - id: 0
              name: Research Group One
            - id: 1
              name: Research Group Two
    """

    return ""
