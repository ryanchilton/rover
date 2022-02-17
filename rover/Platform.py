import board
import math
from DriveWheel import DriveWheel

class Platform:
    def __init__(self):
        
        self.wheel_fl = DriveWheel(4, reverse = True)
        self.wheel_fr = DriveWheel(3, reverse = True)
        self.wheel_bl = DriveWheel(1, reverse = False)
        self.wheel_br = DriveWheel(2, reverse = False)

        print('constructed platform')

    def stop(self):
        self.wheel_fl.setSpeed(0)
        self.wheel_fr.setSpeed(0)
        self.wheel_bl.setSpeed(0)
        self.wheel_br.setSpeed(0)

    def forward(self, effort):
        self.wheel_fl.setSpeed(effort)
        self.wheel_fr.setSpeed(effort)
        self.wheel_bl.setSpeed(effort)
        self.wheel_br.setSpeed(effort)

    def right(self, effort):
        self.wheel_fl.setSpeed(-effort)
        self.wheel_fr.setSpeed(effort)
        self.wheel_bl.setSpeed(effort)
        self.wheel_br.setSpeed(-effort)
        
    def translate(self, angle_rad, effort):
        roller_angle = math.pi/4.0
        
        self.wheel_fl.setSpeed(math.cos(angle_rad - roller_angle) * effort)
        self.wheel_fr.setSpeed(math.cos(angle_rad + roller_angle) * effort)
        self.wheel_bl.setSpeed(math.cos(angle_rad + roller_angle) * effort)
        self.wheel_br.setSpeed(math.cos(angle_rad - roller_angle) * effort)
        
    
    # postive in CW direction
    def rotate(self, effort):
        self.wheel_fl.setSpeed(effort)
        self.wheel_fr.setSpeed(-effort)
        self.wheel_bl.setSpeed(effort)
        self.wheel_br.setSpeed(-effort)
        
        


