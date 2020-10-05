from .game import Game
from .robot import Robot
from .command_invoker import CommandInvoker
from .move import Move


class Driver:

    @staticmethod
    def run():
        game = Game(Robot())
        command_invoker = CommandInvoker(game.current_robot)
        print("Hello! Robot coming online.")
        print("Command the robot with:")
        print(command_invoker)
        _continue = True
        while _continue:
            # if game has multiple robots than first change game.current_robot
            # then
            # command_invoker = CommandInvoker(game.current_robot)
            command = input()
            try:
                command_obj = command_invoker.get_command(command)
            except Exception:
                print("Please enter valid command")
                continue
            response = command_obj.execute()
            if response.success:
                game.add_move(Move(command_obj, game.current_robot))
            else:
                # For now, letting pass this condition. Can raise exception
                pass

            if response.terminate:
                _continue = False

        print("Robot shutting down.")
