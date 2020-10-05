from .interfaces.command_interface import CommandInterface
from .interfaces.robot_interface import RobotInterface
from .command_response import CommandResponse


class CommandList(CommandInterface):
    def __init__(self, robot: RobotInterface):
        self._robot = robot

    @property
    def command(self):
        return "?"

    @property
    def description(self):
        return "print this message"

    @property
    def robot(self):
        return self._robot

    # Need to re-think how to handle this scenario
    def execute(self) -> CommandResponse:
        from .command_invoker import CommandInvoker
        print("Command the robot with:")
        print(CommandInvoker(self.robot))
        return CommandResponse()

    # We can add this feature as well
    def undo(self):
        pass
