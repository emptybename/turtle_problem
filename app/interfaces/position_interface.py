from abc import ABC, abstractmethod


class PositionInterface(ABC):

    @property
    @abstractmethod
    def facing(self): pass
