from .interfaces.position_interface import PositionInterface


class Position(PositionInterface):

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def facing(self):
        pass

    def turn_left(self): pass

    def turn_right(self): pass

    def move_forward(self): pass
