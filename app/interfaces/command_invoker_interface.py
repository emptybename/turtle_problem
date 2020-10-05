from abc import ABC, abstractmethod
from .command_interface import CommandInterface
from typing import Optional


class CommandInvokerInterface(ABC):

    @abstractmethod
    def get_command(self, command: str) -> Optional[CommandInterface]:
        pass
