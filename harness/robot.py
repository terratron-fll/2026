from pybricks.hubs import PrimeHub
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.robotics import DriveBase

class Robot:
    """
    A class to represent our team's robot.
    This helps us share the same motor and sensor setup across all missions.
    """
    def __init__(self) -> None:
        # Initialize the Hub
        self.hub = PrimeHub()

        # Initialize Motors
        # Adjust ports (Port.A, Port.B, etc.) and directions based on your robot build
        self.left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.B)
        
        # Initialize DriveBase for moving and turning
        # wheel_diameter and wheel_track are in mm
        self.drive_base = DriveBase(self.left_motor, self.right_motor, wheel_diameter=56, wheel_track=114)

        # Initialize Sensors
        # self.color_sensor = ColorSensor(Port.C)

    def stop(self) -> None:
        """Stops the robot safely."""
        self.drive_base.stop()
        self.left_motor.brake()
        self.right_motor.brake()

    def beep(self) -> None:
        """Plays a sound to show the robot is ready."""
        self.hub.speaker.beep()
