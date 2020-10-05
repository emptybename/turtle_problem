from abc import ABC, abstractmethod
from .position_interface import PositionInterface


class RobotInterface(ABC):

    @property
    @abstractmethod
    def current_position(self) -> PositionInterface: pass

    @current_position.setter
    @abstractmethod
    def current_position(self, position: PositionInterface): pass

    @abstractmethod
    def turn_left(self) -> None: pass

    @abstractmethod
    def turn_right(self) -> None: pass

    @abstractmethod
    def move_forward(self) -> None: pass
