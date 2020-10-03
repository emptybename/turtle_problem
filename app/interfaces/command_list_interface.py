from abc import abstractmethod
from .command_interface import CommandInterface
from typing import Optional


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class CommandListInterface(metaclass=Singleton):

    @abstractmethod
    def get_command_obj(self, command: str) -> Optional[CommandInterface]:
        pass

    @abstractmethod
    def add_command(self, command: str, description: str, command_obj: CommandInterface) -> None:
        pass
