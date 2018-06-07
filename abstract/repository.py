from abc import ABC, abstractmethod


class Repository():
    """Abstract class for repositories"""

    def __init__(self, storage):
        self.storage = storage()

    def get_all(self):
        return self.storage.get()

