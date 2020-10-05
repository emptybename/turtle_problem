from abc import ABC, abstractmethod
from .robot_interface import RobotInterface
from ..move import Move
from typing import List


class GameInterface(ABC):

    # @abstractmethod
    # def add_robot(self, robot: RobotInterface): pass

    @property
    @abstractmethod
    def moves(self) -> List[Move]: pass

    @abstractmethod
    def add_move(self, move: Move): pass

    @property
    @abstractmethod
    def current_robot(self) -> RobotInterface: pass
