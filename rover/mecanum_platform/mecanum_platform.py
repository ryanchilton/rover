import board
import math
from .drive_wheel import DriveWheel
from .drive_effort import DriveEffort
from .motion_effort import MotionEffort

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
        
    def computeTranslationEffort(self, x_effort, y_effort):
        roller_angle = math.pi/4.0
        
        effort_angle = math.atan2(y_effort, x_effort)
        effort_magnitude = math.sqrt(x_effort**2 + y_effort**2)
        
        fl = math.cos(effort_angle - roller_angle) * effort_magnitude
        fr = math.cos(effort_angle + roller_angle) * effort_magnitude
        bl = math.cos(effort_angle + roller_angle) * effort_magnitude
        br = math.cos(effort_angle - roller_angle) * effort_magnitude
        
        return DriveEffort(effort_fl = fl, effort_fr = fr, effort_bl = bl, effort_br = br)
    
    def computeRotationEffort(self, effort):
        # postive in CW direction
        fl = effort
        fr = -effort
        bl = effort
        br = -effort
        
        return DriveEffort(effort_fl = fl, effort_fr = fr, effort_bl = bl, effort_br = br)

        
    def translate(self, x_effort, y_effort):
        platform_effort = self.computeTranslationEffort(x_effort, y_effort)
        self.execute(platform_effort)
        
    
    # postive in CW direction
    def rotate(self, effort):
        platform_effort = self.computeRotationEffort(effort)
        self.execute(platform_effort)
        
    def twist(self, motion_effort):
        eff1 = self.computeTranslationEffort(motion_effort.linear_x, motion_effort.linear_y)
        eff2 = self.computeRotationEffort(motion_effort.rotational_z)
        
        superposition = eff1 + eff2
        superposition.normalize()
        
        self.execute(superposition)
        
    def execute(self, command):
        self.wheel_fl.setSpeed(command.getEffortFL())
        self.wheel_fr.setSpeed(command.getEffortFR())
        self.wheel_bl.setSpeed(command.getEffortBL())
        self.wheel_br.setSpeed(command.getEffortBR())
        
        


