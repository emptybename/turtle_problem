from abc import ABC, abstractmethod
from .response_interface import ResponseInterface


class CommandInterface(ABC):

    @abstractmethod
    def execute(self) -> ResponseInterface: pass
