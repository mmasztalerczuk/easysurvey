from abstract.storage import Storage


class TestRepository(Storage):
    def __init__(self):
        self.data = []

    def put(self, item):
        self.data.append(item)

    def get(self):
        return self.data

