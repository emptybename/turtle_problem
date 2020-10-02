from .interfaces.game_interface import GameInterface
from .interfaces.robot_interface import RobotInterface
from .interfaces.move_interface import MoveInterface
from typing import List


class Game(GameInterface):
    def __init__(self, robot: RobotInterface):
        self._moves = []
        self._current_robot = robot

    def moves(self) -> List[MoveInterface]:
        return self._moves

    def add_move(self, move: MoveInterface):
        self._moves.append(move)

    @property
    def current_robot(self) -> RobotInterface:
        return self._current_robot
