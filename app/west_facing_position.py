from .position import Position
# from .north_facing_position import NorthFacingPosition
# from .south_facing_position import SouthFacingPosition


class WestFacingPosition(Position):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    @property
    def facing(self):
        return "West"

    def turn_left(self):
        from .south_facing_position import SouthFacingPosition
        return SouthFacingPosition(self.x, self.y)

    def turn_right(self):
        from .north_facing_position import NorthFacingPosition
        return NorthFacingPosition(self.x, self.y)

    def move_forward(self):
        return WestFacingPosition(self.x - 1, self.y)
