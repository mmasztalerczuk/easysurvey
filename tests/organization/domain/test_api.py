from organization import create_new_unit


def test_create_new_unit(mocker):
    m_unit_factory = mocker.patch("organization.UnitFactory")
    m_unit = mocker.Mock()
    m_unit_factory.build.return_value = m_unit

    name = "Unit 1"

    expect_unit = create_new_unit(name)

    assert expect_unit == m_unit
