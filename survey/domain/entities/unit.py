import logging

import uuid

from abstract.enities import Entity
from abstract.factory import Factory
from survey.domain.entities.new_research_group import ResearchGroupFactory

logger = logging.getLogger(__name__)


class Unit(Entity):

    def create_new_research_group(self, name):
        return ResearchGroupFactory.build(name)


class UnitFactory(Factory):
    """Unit factory"""

    @staticmethod
    def build(name):
        logger.debug("Building new unit")
        unit = Unit(uuid.uuid4(), name)
        logger.debug("Finished building new unit id: {unit.id}")
        return unit