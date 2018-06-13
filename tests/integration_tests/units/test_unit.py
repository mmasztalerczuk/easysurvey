from aggregations.organization import UnitFactory
from aggregations.organization.domain.entities.unit import UnitRepository
from infrastructure.ctx import UnitOfWork


def test_create_unit():
    name = "New Unit"

    temp = []

    class MockStorage:
        def put(self, x):
            temp.append(x)

    with UnitOfWork(MockStorage) as ctx:
        unit = UnitFactory.build(name)
        ctx.use(UnitRepository).put(unit)

        assert temp[0] == unit