from abstract.factory import Factory
from survey.domain.entities.unit import Unit


class UnitFactory(Factory):

    @staticmethod
    def build(name):
        unit = Unit(name)
        return unit
