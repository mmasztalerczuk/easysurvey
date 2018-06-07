from survey import create_new_unit

def test_create_new_unit(mocker):
    m_unit_factory = mocker.patch("survey.UnitFactory")
    m_unit = mocker.Mock()
    m_id = 1

    m_unit.id = m_id
    m_unit_factory.build.return_value = m_unit

    name = "Unit 1"

    expect_id = create_new_unit(name)

    assert expect_id == m_id