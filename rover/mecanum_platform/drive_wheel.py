import time
from Adafruit_MotorHAT import Adafruit_MotorHAT as motor_driver


class DriveWheel:
    def __init__(self, motor_index, reverse = False):
        driver = motor_driver(i2c_bus = 1)
        self.motor = driver.getMotor(motor_index)
        self.reverse = reverse
        print('constructed motor')


    # speed range: [-1.0, 1.0]
    def setSpeed(self, effort):
        
        cmd = self.effortToCommand(effort)
        
        if (self.reverse):
            cmd = -cmd

        if cmd < 0:
            self.motor.run(motor_driver.BACKWARD)
        else:
            self.motor.run(motor_driver.FORWARD)

        self.motor.setSpeed(abs(int(cmd)))

    def effortToCommand(self, effort):
        return 255 * max(-1.0, min(1.0, effort))