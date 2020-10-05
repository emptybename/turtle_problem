from .interfaces.response_interface import ResponseInterface


class CommandResponse:
    def __init__(self, success=True, terminate=False):
        self._success = success
        self._terminate = terminate

    @property
    def success(self):
        return self._success

    @property
    def terminate(self):
        return self._terminate
