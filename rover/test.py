# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Simple test for using adafruit_motorkit with a DC motor"""
import time
import board
from Adafruit_MotorHAT import Adafruit_MotorHAT as motor_driver


class DriveWheel:
    def __init__(self, motor, reverse = False):
        self.motor = motor
        self.reverse = reverse
        print('constructed motor')


    def setSpeed(self, speed):
        if (self.reverse):
            speed = -speed

        if speed < 0:
            self.motor.run(motor_driver.BACKWARD)
        else:
            self.motor.run(motor_driver.FORWARD)

        self.motor.setSpeed(abs(int(speed)))

class Platform:
    def __init__(self):
        driver = motor_driver(i2c_bus = 1)
        self.wheel_fl = DriveWheel(driver.getMotor(4), reverse = True)
        self.wheel_fr = DriveWheel(driver.getMotor(3), reverse = True)
        self.wheel_bl = DriveWheel(driver.getMotor(1), reverse = False)
        self.wheel_br = DriveWheel(driver.getMotor(2), reverse = False)

        print('constructed platform')

    def stop(self):
        self.wheel_fl.setSpeed(0)
        self.wheel_fr.setSpeed(0)
        self.wheel_bl.setSpeed(0)
        self.wheel_br.setSpeed(0)

    def forward(self, effort):
        effort = max(-1.0, min(1.0, effort))
        speed_command = 255 * effort

        self.wheel_fl.setSpeed(speed_command)
        self.wheel_fr.setSpeed(speed_command)
        self.wheel_bl.setSpeed(speed_command)
        self.wheel_br.setSpeed(speed_command)

    def right(self, effort):
        effort = max(-1.0, min(1.0, effort))
        speed_command = 255 * effort

        self.wheel_fl.setSpeed(-speed_command)
        self.wheel_fr.setSpeed(speed_command)
        self.wheel_bl.setSpeed(speed_command)
        self.wheel_br.setSpeed(-speed_command)

platform = Platform()
platform.forward(-0.5)
time.sleep(1)
platform.stop()
time.sleep(1)
platform.right(0.5)
time.sleep(1)
platform.stop()
