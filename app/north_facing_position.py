from .position import Position


class NorthFacingPosition(Position):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    @property
    def facing(self):
        return "North"
