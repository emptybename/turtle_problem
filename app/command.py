from .interfaces.command_interface import CommandInterface
from .interfaces.game_interface import GameInterface
from .interfaces.manager.command_manager_interface import CommandManagerInterface


class Command(CommandInterface):

    def execute(self, game: GameInterface, manager: CommandManagerInterface) -> bool: pass
