from .interfaces.position_interface import PositionInterface


class Position(PositionInterface):

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def facing(self): pass

    def move_left(self):
        pass

    def move_right(self):
        pass

    def move_forward(self):
        pass
