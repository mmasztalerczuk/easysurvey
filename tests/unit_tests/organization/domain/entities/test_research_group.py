from aggregations.organization.domain.entities.research_group import ResearchGroup


def test_add_survey_to_reseach_group():
    research_group_name = "test"
    survey_name = "survey name"

    research_group = ResearchGroup(1, research_group_name, None)

    new_survey = research_group.create_new_survey(survey_name)

    assert new_survey.name == survey_name