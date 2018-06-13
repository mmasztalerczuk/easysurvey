
class UnitOfWork:
    def __init__(self, persistent_storage):
        self._persistent_storage = persistent_storage

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        pass

    def use(self, cls):
        return cls(self._persistent_storage)
