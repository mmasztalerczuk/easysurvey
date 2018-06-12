from flask import Blueprint, request

view = Blueprint('view3', __name__)


@view.route("/participant/research_group", methods=['POST'])
def research_group():
    """
    Join to research group
    ---
    definitions:
      - schema:
          id: JoinResearchGroup
          properties:
            research_group_code:
              type: string
              description: access code of research group (6 chars)
              example: AXDE23
            name:
              type: string
              description: the name of research group code
            description:
              type: string
              description: more information about research group

    security:
      - Participant: []
    tags:
      - participant
    parameters:
      - in: body
        name: body
        schema:
          $ref: '#/definitions/JoinResearchGroup'
        examples:
          one:
            name: "Unit One"
    responses:
      201:
        description: Unit created
      500:
        description: Internal Error
    """
    return ""


@view.route("/participant/research_group", methods=['GET'])
def get_research_group():
    """
    Get all research groups of participant
    ---
    security:
      - Participant: []
    tags:
      - participant
    responses:
      200:
        description: Get all research groups of participant
        schema:
          type: array
          items:
            $ref: '#/definitions/JoinResearchGroup'
          example:
            - code: ABCEDF
              name: Best pet research
              description: We are looking for best pet research
            - id: WES234
              name: Worst pet research
              description: We are looking for worst pet research
    """

    return ""
