from .game import Game
from .robot import Robot
from .command_list import CommandList


class Driver:

    @staticmethod
    def run():
        game = Game(Robot())
        command_list = CommandList()
        print("Command the robot with:")
        print(command_list)
        _continue = True
        while _continue:
            command = input()
            command_obj = command_list.get_command_obj(command)
            if not command_obj:
                print("Please enter valid input")
            elif not command_obj.execute(game):
                _continue = False
        print("Robot shutting down.")
