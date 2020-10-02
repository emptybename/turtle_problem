from .interfaces.robot_interface import RobotInterface
from .interfaces.move_interface import MoveInterface


class Move(MoveInterface):
    def __init__(self, robot: RobotInterface):
        self._initial_position = robot.current_position
        self._final_position = None
        self._robot = robot

    @property
    def initial_position(self):
        return self._initial_position

    @property
    def robot(self):
        return self._robot

    @property
    def final_position(self):
        return self._final_position

    @final_position.setter
    def final_position(self, final_position):
        self._final_position = final_position
