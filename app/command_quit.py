from .command import Command
from .interfaces.game_interface import GameInterface


class CommandQuit(Command):
    def execute(self, game: GameInterface) -> bool:
        return False
