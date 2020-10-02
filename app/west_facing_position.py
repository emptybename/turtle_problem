from .position import Position


class WestFacingPosition(Position):
    def __init__(self, x, y):
        super().__init__(x, y)

    @property
    def facing(self):
        return "West"

    def move_left(self):
        from .south_facing_position import SouthFacingPosition
        return SouthFacingPosition(self.x, self.y)

    def move_right(self):
        from .north_facing_position import NorthFacingPosition
        return NorthFacingPosition(self.x, self.y)

    def move_forward(self):
        self.x -= 1
        return self
