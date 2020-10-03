from abc import ABC, abstractmethod
from .game_interface import GameInterface
from .manager.command_manager_interface import CommandManagerInterface


class CommandInterface(ABC):

    @abstractmethod
    def execute(self, game: GameInterface, manager: CommandManagerInterface) -> bool: pass
