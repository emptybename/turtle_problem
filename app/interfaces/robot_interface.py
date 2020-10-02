from abc import ABC, abstractmethod
from .position_interface import PositionInterface


class RobotInterface(ABC):

    @property
    @abstractmethod
    def current_position(self): pass

    @abstractmethod
    def set_current_position(self, position: PositionInterface): pass
