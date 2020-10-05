from abc import ABC, abstractmethod


class PositionInterface(ABC):

    @property
    @abstractmethod
    def facing(self): pass

    @abstractmethod
    def turn_left(self): pass

    @abstractmethod
    def turn_right(self): pass

    @abstractmethod
    def move_forward(self): pass
