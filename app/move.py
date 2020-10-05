from .interfaces.robot_interface import RobotInterface
from .interfaces.command_interface import CommandInterface


class Move:
    def __init__(self, command: CommandInterface, robot: RobotInterface):
        self._command = command
        self._robot = robot

    @property
    def command(self):
        return self._command

    @property
    def robot(self):
        return self._robot
