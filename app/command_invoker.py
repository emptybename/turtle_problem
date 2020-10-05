from .interfaces.command_invoker_interface import CommandInvokerInterface
from .interfaces.command_interface import CommandInterface
from .interfaces.robot_interface import RobotInterface
from .exceptions.exceptions import InvalidInput
from .commandl import CommandL
from .commandr import CommandR
from .commandm import CommandM
from .command_list import CommandList
from .commandq import CommandQ
from typing import Optional


class CommandInvoker(CommandInvokerInterface, list):
    def __init__(self, robot: RobotInterface):
        super().__init__(self)
        self.append(CommandL(robot))
        self.append(CommandR(robot))
        self.append(CommandM(robot))
        self.append(CommandList(robot))
        self.append(CommandQ(robot))

    def get_command(self, command: str) -> Optional[CommandInterface]:
        for command_obj in self:
            # print(command_obj.command, command)
            # print(command_obj.command == command)
            if command_obj.command == command:
                return command_obj

        raise InvalidInput

    def __str__(self):
        commands_list = []
        for command_obj in self:
            commands_list.append(command_obj.command + ' - ' + command_obj.description)
        return '\n'.join(commands_list)
