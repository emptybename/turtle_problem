from .position import Position


class NorthFacingPosition(Position):
    def __init__(self, x, y):
        super().__init__(x, y)

    @property
    def facing(self):
        return "North"

    def move_left(self):
        from .west_facing_position import WestFacingPosition
        return WestFacingPosition(self.x, self.y)

    def move_right(self):
        from .east_facing_position import EastFacingPosition
        return EastFacingPosition(self.x, self.y)

    def move_forward(self):
        self.y += 1
        return self
