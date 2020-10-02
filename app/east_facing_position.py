from .position import Position


class EastFacingPosition(Position):
    def __init__(self, x, y):
        super().__init__(x, y)

    @property
    def facing(self):
        return "East"

    def move_left(self):
        from .north_facing_position import NorthFacingPosition
        return NorthFacingPosition(self.x, self.y)

    def move_right(self):
        from .south_facing_position import SouthFacingPosition
        return SouthFacingPosition(self.x, self.y)

    def move_forward(self):
        self.x += 1
        return self
