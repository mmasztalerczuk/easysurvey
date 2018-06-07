import logging

import uuid

from abstract.enities import Entity
from abstract.factory import Factory

logger = logging.getLogger(__name__)


class ResearchGroup(Entity):
    pass


class ResearchGroupFactory(Factory):
    """New Research Group Factory"""

    @staticmethod
    def build(name):
        logger.debug("Building new research group unit")
        unit = ResearchGroup(uuid.uuid4(), name)
        logger.debug("Finished building new research group id: {unit.id}")
        return unit
