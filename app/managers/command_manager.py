from ..interfaces.robot_interface import RobotInterface
from ..south_facing_position import SouthFacingPosition
from ..north_facing_position import NorthFacingPosition
from ..west_facing_position import WestFacingPosition
from ..east_facing_position import EastFacingPosition


class CommandManager:

    @staticmethod
    def turn_left(robot: RobotInterface, steps=0):
        if robot.current_position.facing == SouthFacingPosition().facing:
            new_position = EastFacingPosition(
                robot.current_position.x + steps, robot.current_position.y
            )
        elif robot.current_position.facing == EastFacingPosition().facing:
            new_position = NorthFacingPosition(
                robot.current_position.x, robot.current_position.y + steps
            )
        elif robot.current_position.facing == NorthFacingPosition().facing:

            new_position = WestFacingPosition(
                robot.current_position.x - steps, robot.current_position.y
            )
        else:
            new_position = SouthFacingPosition(
                robot.current_position.x, robot.current_position.y - steps
            )
        return new_position

    @staticmethod
    def turn_right(robot: RobotInterface, steps=0):
        if robot.current_position.facing == SouthFacingPosition().facing:
            new_position = WestFacingPosition(
                robot.current_position.x - steps, robot.current_position.y
            )
        elif robot.current_position.facing == EastFacingPosition().facing:
            new_position = SouthFacingPosition(
                robot.current_position.x, robot.current_position.y - steps
            )
        elif robot.current_position.facing == NorthFacingPosition().facing:
            new_position = EastFacingPosition(
                robot.current_position.x + steps, robot.current_position.y
            )
        else:
            new_position = NorthFacingPosition(
                robot.current_position.x, robot.current_position.y + steps
            )
        return new_position

    @staticmethod
    def move_forward(robot: RobotInterface, steps=1):
        if robot.current_position.facing == SouthFacingPosition().facing:
            new_position = SouthFacingPosition(
                robot.current_position.x, robot.current_position.y - steps
            )
        elif robot.current_position.facing == EastFacingPosition().facing:
            new_position = EastFacingPosition(
                robot.current_position.x + steps, robot.current_position.y
            )
        elif robot.current_position.facing == NorthFacingPosition().facing:
            new_position = NorthFacingPosition(
                robot.current_position.x, robot.current_position.y + steps
            )
        else:
            new_position = WestFacingPosition(
                robot.current_position.x - steps, robot.current_position.y
            )
        return new_position
