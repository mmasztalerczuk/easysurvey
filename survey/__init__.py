from survey.domain.factory import UnitFactory


def create_new_unit(name):
    return UnitFactory.build(name).id

