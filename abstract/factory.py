from abc import ABC, abstractmethod


class Factory(ABC):
    """Abstract class for factory
    """
    @abstractmethod
    def build(self):
        pass
