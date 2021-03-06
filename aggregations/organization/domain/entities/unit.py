import logging
import uuid
from abc import ABCMeta, abstractmethod
from functools import singledispatch

from abstract.domain_event import DomainEvent
from abstract.enities import Entity
from abstract.factory import Factory
from abstract.repository import Repository
from aggregations.organization.domain.entities.research_group import ResearchGroupFactory

logger = logging.getLogger(__name__)


class Unit(Entity):
    """The unit that represents the highest organizational unit in the hierarchy.

       He is responsible for the creation of new research groups and is the place that determines
       the researcher's affiliation
    """

    class CreatedResearchGroup(DomainEvent):
        pass

    def create_new_research_group(self, name, code=None, description=None):
        """
        Creates a new research group. The process of creating a new group requires a name.
        The name will be visible to participants of the study.
        Each research group is recognized by the participants of the study by means of a code.
        This code can be given manually, but it can also be generated randomly.

        Args:
            name (str): The name of new research group. This will be visible for participants
            code (str, optional): This code which will be use to join to research group by participants.
            description (str, optional): The description of research group. This will be visible for participants.

        Returns:
            New created research group

        Raises:
            None
        """
        event = Unit.CreatedResearchGroup(aggregate_id=self._id,
                                          name=name,
                                          code=code,
                                          description=description)

        self._apply(event)
        self.publish(event)

        research_group = ResearchGroupFactory.build(name)
        return research_group

    @singledispatch
    def _when(self, event):
        pass


class UnitFactory(Factory):
    """Unit factory"""

    @staticmethod
    def build(name):
        logger.debug("Building new unit")

        unit = Unit(uuid.uuid4(), name)

        logger.debug("Finished building new unit id: {unit.id}")
        return unit
