from abstract.repository import Repository


class UnitRepository(Repository):

    def put(self, unit):
        _persistent_storage.append()
