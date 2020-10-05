from .position import Position
from .east_facing_position import EastFacingPosition
from .west_facing_position import WestFacingPosition


class SouthFacingPosition(Position):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    @property
    def facing(self):
        return "South"

    def turn_left(self):
        return EastFacingPosition(self.x, self.y)

    def turn_right(self):
        return WestFacingPosition(self.x, self.y)

    def move_forward(self):
        return SouthFacingPosition(self.x, self.y - 1)
