from abc import ABC, abstractmethod
from .position_interface import PositionInterface


class MoveInterface(ABC):

    @property
    @abstractmethod
    def initial_position(self): pass

    @property
    @abstractmethod
    def final_position(self): pass

    @final_position.setter
    @abstractmethod
    def final_position(self, position: PositionInterface): pass

    @property
    @abstractmethod
    def robot(self): pass
