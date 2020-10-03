from .command import Command
from .interfaces.game_interface import GameInterface
from .managers.command_manager import CommandManager


class CommandQ(Command):
    def execute(self, game: GameInterface, manager=CommandManager()) -> bool:
        from .command_list import CommandList
        print("Command the robot with:")
        print(CommandList())
        return True
