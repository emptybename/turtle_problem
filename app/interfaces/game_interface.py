from abc import ABC, abstractmethod
from .robot_interface import RobotInterface
from .move_interface import MoveInterface
from typing import List


class GameInterface(ABC):

    # @abstractmethod
    # def add_robot(self, robot: RobotInterface): pass

    @property
    @abstractmethod
    def moves(self) -> List[MoveInterface]: pass

    @abstractmethod
    def add_move(self, move: MoveInterface): pass

    @property
    @abstractmethod
    def current_robot(self) -> RobotInterface: pass
