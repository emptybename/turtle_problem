from .interfaces.command_interface import CommandInterface
from .interfaces.game_interface import GameInterface


class Command(CommandInterface):
    COMMAND_LIST = []

    class CommandType:
        def __init__(self, identifier, description, _class):
            self._identifier = identifier
            self._description = description
            self._class = _class

        @property
        def get_class(self):
            return self._class

        @property
        def identifier(self):
            return self._identifier

        @property
        def description(self):
            return self._description

    def execute(self, game: GameInterface) -> bool: pass

    def is_valid(self, command) -> bool:
        return command in [command_type.identifier for command_type in self.COMMAND_LIST]

    def add_command(self, identifier: str, description: str, _class: str) -> None:
        self.COMMAND_LIST.append(self.CommandType(identifier, description, _class))
