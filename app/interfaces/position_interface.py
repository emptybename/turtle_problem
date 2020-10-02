from abc import ABC, abstractmethod


class PositionInterface(ABC):

    @property
    @abstractmethod
    def facing(self): pass

    @abstractmethod
    def move_left(self):
        pass

    @abstractmethod
    def move_right(self):
        pass

    @abstractmethod
    def move_forward(self):
        pass
