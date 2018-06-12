from flask import Blueprint, request

view = Blueprint('results', __name__)


@view.route("/participant/results", methods=['GET'])
def results():
    """
    Get all research groups of participant
    ---
    security:
      - Participant: []
    tags:
      - results
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
