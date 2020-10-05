from .interfaces.command_interface import CommandInterface
from .interfaces.robot_interface import RobotInterface
from .command_response import CommandResponse


class CommandR(CommandInterface):
    def __init__(self, robot: RobotInterface):
        self._robot = robot

    @property
    def command(self):
        return "R"

    @property
    def description(self):
        return "turn right"

    @property
    def robot(self):
        return self._robot

    def execute(self) -> CommandResponse:
        self.robot.turn_right()
        print(self.robot)
        return CommandResponse()

    # We can add this feature as well
    def undo(self):
        pass
