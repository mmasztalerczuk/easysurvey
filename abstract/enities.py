import logging

from abc import ABC

logger = logging.getLogger(__name__)


class Entity(ABC):
    """Abstract class for factory"""

    def __init__(self, new_id, name):
        logger.debug(f"New entity id: {new_id} name: {name}")
        self._id = new_id
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id
