from abstract.factory import Factory
from aggregations.organization import UnitFactory
from infrastructure.ctx import ctx
from infrastructure.repositories.testrepository import TestRepository


def test_is_unit_factory_a_factory():
    assert isinstance(UnitFactory(), Factory)


def test_build_new_unit():
    name = "Unit 1"
    with ctx(TestRepository):
        new_unit = UnitFactory.build(name)

    assert new_unit.name == name
