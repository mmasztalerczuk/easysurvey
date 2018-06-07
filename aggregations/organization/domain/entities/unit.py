import logging

import uuid

from abstract.enities import Entity
from abstract.factory import Factory
from abstract.repository import Repository
from aggregations.organization.domain.entities.research_group import ResearchGroupFactory
from infrastructure.ctx import get_ctx_storage

logger = logging.getLogger(__name__)


class Unit(Entity):

    def create_new_research_group(self, name):
        r = ResearchGroupFactory.build(name)
        self.repository.save_research_group(r)

        return r

    def get_all_research_group(self):
        return self.repository.get_all()


class UnitFactory(Factory):
    """Unit factory"""

    @staticmethod
    def build(name):
        logger.debug("Building new unit")
        unit = Unit(uuid.uuid4(), name)

        unit.repository = UnitRepository(get_ctx_storage())

        logger.debug("Finished building new unit id: {unit.id}")
        return unit


class UnitRepository(Repository):

    def save_research_group(self, research_group):
        self.storage.put(research_group)

