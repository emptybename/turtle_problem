from abc import ABC, abstractmethod
from ..robot_interface import RobotInterface
from ..position_interface import PositionInterface


class CommandManagerInterface(ABC):

    @staticmethod
    @abstractmethod
    def turn_left(robot: RobotInterface, steps: int) -> PositionInterface:
        pass

    @staticmethod
    @abstractmethod
    def turn_right(robot: RobotInterface, steps: int) -> PositionInterface:
        pass

    @staticmethod
    @abstractmethod
    def move_forward(robot: RobotInterface, steps: int) -> PositionInterface:
        pass
