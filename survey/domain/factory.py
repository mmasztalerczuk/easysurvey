import uuid
import logging

from abstract.factory import Factory
from survey.domain.entities.unit import Unit

logger = logging.getLogger(__name__)


class UnitFactory(Factory):
    """Unit factory"""

    @staticmethod
    def build(name):
        logger.debug("Building new unit")
        unit = Unit(uuid.uuid4(), name)
        logger.debug("Finished building new unit id: {unit.id}")
        return unit
