import board
import math
from .DriveWheel import DriveWheel
from .PlatformEffort import PlatformEffort

class MecanumPlatform:
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
        
    def computeTranslationEffort(self, angle_rad, effort):
        roller_angle = math.pi/4.0
        
        fl = math.cos(angle_rad - roller_angle) * effort
        fr = math.cos(angle_rad + roller_angle) * effort
        bl = math.cos(angle_rad + roller_angle) * effort
        br = math.cos(angle_rad - roller_angle) * effort
        
        return PlatformEffort(effort_fl = fl, effort_fr = fr, effort_bl = bl, effort_br = br)
    
    def computeRotationEffort(self, effort):
        # postive in CW direction
        fl = effort
        fr = -effort
        bl = effort
        br = -effort
        
        return PlatformEffort(effort_fl = fl, effort_fr = fr, effort_bl = bl, effort_br = br)

        
    def translate(self, angle_rad, effort):
        platform_effort = self.computeTranslationEffort(angle_rad, effort)
        self.execute(platform_effort)
        
    
    # postive in CW direction
    def rotate(self, effort):
        platform_effort = self.computeRotationEffort(effort)
        self.execute(platform_effort)
        
    def twist(self, linear_direction, linear_effort, rotational_effort):
        eff1 = self.computeTranslationEffort(linear_direction, linear_effort)
        eff2 = self.computeRotationEffort(rotational_effort)
        
        superposition = eff1 + eff2
        superposition.normalize()
        
        self.execute(superposition)
        
    def execute(self, command):
        self.wheel_fl.setSpeed(command.getEffortFL())
        self.wheel_fr.setSpeed(command.getEffortFR())
        self.wheel_bl.setSpeed(command.getEffortBL())
        self.wheel_br.setSpeed(command.getEffortBR())
        
        


