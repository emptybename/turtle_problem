from .interfaces.robot_interface import RobotInterface
from .position import Position
from .north_facing_position import NorthFacingPosition


class Robot(RobotInterface):

    def __init__(self, position=NorthFacingPosition(0, 0)):
        self._current_position = position

    @property
    def current_position(self) -> Position:
        return self._current_position

    @current_position.setter
    def current_position(self, position: Position) -> None:
        self._current_position = position

    def turn_left(self):
        self.current_position = self.current_position.turn_left()

    def turn_right(self):
        self.current_position = self.current_position.turn_right()

    def move_forward(self):
        self.current_position = self.current_position.move_forward()

    def __str__(self):
        return (
            f'Robot at ({self._current_position.x}, {self._current_position.y}) facing {self._current_position.facing}'
        )
