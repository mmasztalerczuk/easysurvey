from flask import Blueprint, request

view = Blueprint('news_feed', __name__)


@view.route("/participant/news", methods=['GET'])
def news():
    """
    Get all research groups of participant
    ---
    security:
      - Participant: []
    tags:
      - news feed
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
