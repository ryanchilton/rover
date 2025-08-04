from mecanum_platform import MecanumPlatform
from teleop.teleop_interface import TeleopInterface

if __name__ == "__main__":
    platform = MecanumPlatform()
    teleop_interface = TeleopInterface(platform)
    teleop_interface.loop()

    