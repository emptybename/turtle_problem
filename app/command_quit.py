from .command import Command
from .interfaces.game_interface import GameInterface
from .managers.command_manager import CommandManager


class CommandQuit(Command):
    def execute(self, game: GameInterface, manager=CommandManager()) -> bool:
        return False
