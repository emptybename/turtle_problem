from .interfaces.command_list_interface import CommandListInterface
from .interfaces.command_interface import CommandInterface
from .commandl import CommandL
from .commandr import CommandR
from .commandm import CommandM
from .commandq import CommandQ
from .command_quit import CommandQuit
from typing import Optional


class CommandList(CommandListInterface, list):
    def __init__(self):
        super().__init__(self)
        # Initial supported commands
        self.append(
            {'command': 'L', 'description': 'turn left', 'command_obj': CommandL()}
        )
        self.append(
            {'command': 'R', 'description': 'turn right', 'command_obj': CommandR()}
        )
        self.append(
            {'command': 'M', 'description': 'move forward', 'command_obj': CommandM()}
        )
        self.append(
            {'command': '?', 'description': 'print this message', 'command_obj': CommandQ()}
        )
        self.append(
            {'command': 'Q', 'description': 'quit', 'command_obj': CommandQuit()}
        )
        print("Hello! Robot coming online.")

    def get_command_obj(self, command: str) -> Optional[CommandInterface]:
        for command_dict in self:
            if command_dict['command'] == command:
                return command_dict['command_obj']
        return None

    def add_command(self, command: str, description: str, command_obj: CommandInterface) -> None:
        self.append({
            'command': command,
            'description': description,
            'command_obj': command_obj
        })

    def __str__(self):
        commands_list = []
        for command in self:
            commands_list.append(command['command'] + ' - ' + command['description'])
        return '\n'.join(commands_list)
