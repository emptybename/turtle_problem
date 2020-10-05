from abc import ABC, abstractmethod


class ResponseInterface(ABC):

    @property
    @abstractmethod
    def success(self): pass

    @property
    @abstractmethod
    def terminate(self): pass
