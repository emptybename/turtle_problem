from .game import Game
from .robot import Robot
from .commandq import CommandQ
from .command import Command
from .factories.command_factory import CommandFactory


class Driver:

    @staticmethod
    def run():
        game = Game(Robot())
        command = Command()
        command.add_command('L', 'turn left', 'CommandL')
        command.add_command('R', 'turn right', 'CommandR')
        command.add_command('?', 'print this message', 'CommandQ')
        command.add_command('M', 'move forward', 'CommandM')
        command.add_command('Q', 'quit', 'CommandQuit')
        print("Hello! Robot coming online.")
        CommandQ().execute(game)
        _continue = True
        while _continue:
            command = input()
            command_obj = CommandFactory().create_command(command)
            if not command_obj:
                print("Please enter valid input")
            elif not command_obj.execute(game):
                _continue = False
        print("Robot shutting down.")
