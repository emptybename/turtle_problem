from .command import Command
from .interfaces.game_interface import GameInterface


class CommandQ(Command):
    def execute(self, game: GameInterface) -> bool:
        print("Command the robot with:")
        for command_type in self.COMMAND_LIST:
            print(command_type.identifier + " - " + command_type.description)
        return True
