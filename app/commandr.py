from .command import Command
from .interfaces.game_interface import GameInterface
from .move import Move
from .managers.command_manager import CommandManager


class CommandR(Command):
    def execute(self, game: GameInterface, manager=CommandManager()) -> bool:
        robot = game.current_robot
        move = Move(robot)
        robot.current_position = manager.turn_right(robot)
        move.final_position = robot.current_position
        game.add_move(move)
        print(robot)
        return True
