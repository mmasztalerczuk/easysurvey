from abc import ABC, abstractmethod


class Storage(ABC):
    """Abstract class for repositories"""

    @abstractmethod
    def get(self):
        raise NotImplementedError
