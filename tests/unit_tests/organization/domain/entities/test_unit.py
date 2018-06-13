from aggregations.organization.domain.entities.unit import Unit, UnitRepository
from infrastructure.ctx import ctx, get_ctx_storage
from infrastructure.repositories.testrepository import TestRepository


def disable_test_create_new_research_group():
    name = "Research group I"

    with ctx(TestRepository):
        new_unit = Unit(1, name, UnitRepository)
        new_unit.repository = UnitRepository(get_ctx_storage())

        new_research_group = new_unit.create_new_research_group(name)

    assert new_research_group.name == name


def disable_test_get_all_research_group():
    name = "Research group I"

    with ctx(TestRepository):
        new_unit = Unit(1, name)
        new_unit.repository = UnitRepository(get_ctx_storage())
        new_unit.create_new_research_group(name)

        assert len(new_unit.get_all_research_group()) == 1
