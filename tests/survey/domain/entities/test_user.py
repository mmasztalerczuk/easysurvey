from survey.domain.entities.unit import Unit


def test_create_new_research_group():
    name = "Research group I"
    new_unit = Unit(1, name)

    new_research_group = new_unit.create_new_research_group(name)

    assert new_research_group.name == name
