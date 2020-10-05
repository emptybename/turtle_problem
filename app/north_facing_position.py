from .position import Position
# from .west_facing_position import WestFacingPosition
# from .east_facing_position import EastFacingPosition


class NorthFacingPosition(Position):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    @property
    def facing(self):
        return "North"

    def turn_left(self):
        from .west_facing_position import WestFacingPosition
        return WestFacingPosition(self.x, self.y)

    def turn_right(self):
        from .east_facing_position import EastFacingPosition
        return EastFacingPosition(self.x, self.y)

    def move_forward(self):
        return NorthFacingPosition(self.x, self.y + 1)
