from ..interfaces.factory.command_factory_interface import CommandFactoryInterface
from ..command import Command
from ..command_quit import CommandQuit
from ..commandq import CommandQ
from ..command_l import CommandL
from ..commandr import CommandR
from ..commandm import CommandM


class CommandFactory(CommandFactoryInterface):

    def create_command(self, command):
        if not Command().is_valid(command):
            return None
        # print(command)
        for command_type in Command().COMMAND_LIST:
            # print(command_type.get_class, command)
            if command_type.identifier == command:
                # print(eval(command_type.get_class)())
                return eval(command_type.get_class)()
