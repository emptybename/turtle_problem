from .interfaces.command_interface import CommandInterface
from .interfaces.robot_interface import RobotInterface
from .command_response import CommandResponse


class CommandL(CommandInterface):
    def __init__(self, robot: RobotInterface):
        self._robot = robot

    @property
    def command(self):
        return "L"

    @property
    def description(self):
        return "turn left"

    @property
    def robot(self):
        return self._robot

    def execute(self) -> CommandResponse:
        self.robot.turn_left()
        print(self.robot)
        return CommandResponse()

    # We can add this feature as well
    def undo(self):
        pass
