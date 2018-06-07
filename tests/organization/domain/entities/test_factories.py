from abstract.factory import Factory
from organization import UnitFactory


def test_is_unit_factory_a_factory():
    assert isinstance(UnitFactory(), Factory)


def test_build_new_unit():
    name = "Unit 1"
    new_unit = UnitFactory.build(name)

    assert new_unit.name == name
