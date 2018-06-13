from abc import abstractmethod, ABCMeta


class Repository(metaclass=ABCMeta):
    """Abstract class for repositories"""

    def __init__(self, _persistent_storage):
        self._persistent_storage = _persistent_storage

    @abstractmethod
    def put(self, research_group):
        raise NotImplementedError
