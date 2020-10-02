from abc import ABC, abstractmethod
from .game_interface import GameInterface


class CommandInterface(ABC):

    @abstractmethod
    def execute(self, game: GameInterface) -> bool: pass
