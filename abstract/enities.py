import logging

from abc import ABC



logger = logging.getLogger(__name__)


class Entity(ABC):
    """Abstract class for factory"""

    def __init__(self, new_id, name, repository=None):
        logger.debug(f"New entity id: {new_id} name: {name}")
        self._id = new_id
        self._name = name
        self._repository = repository

    @property
    def repository(self):
        return self._repository

    @repository.setter
    def repository(self, value):
        self._repository = value

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    def _apply(self, event):
        return self._when(event)


