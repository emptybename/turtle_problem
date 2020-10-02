from .command import Command
from .interfaces.game_interface import GameInterface
from .move import Move


class CommandM(Command):
    def execute(self, game: GameInterface) -> True:
        robot = game.current_robot
        new_position = robot.current_position.move_forward()
        move = Move(robot)
        robot.set_current_position(new_position)
        move.final_position = robot.current_position
        game.add_move(move)
        print(robot)
        return True
