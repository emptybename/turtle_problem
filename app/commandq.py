from .interfaces.command_interface import CommandInterface
from .interfaces.robot_interface import RobotInterface
from .command_response import CommandResponse


class CommandQ(CommandInterface):
    def __init__(self, robot: RobotInterface):
        self._robot = robot

    @property
    def command(self):
        return "Q"

    @property
    def description(self):
        return "quit"

    @property
    def robot(self):
        return self._robot

    def execute(self) -> CommandResponse:
        return CommandResponse(success=True, terminate=True)

    # We can add this feature as well
    def undo(self):
        pass
