from abc import ABC, abstractmethod


class CommandFactoryInterface(ABC):

    @abstractmethod
    def create_command(self, command): pass
