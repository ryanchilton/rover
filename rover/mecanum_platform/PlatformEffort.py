class PlatformEffort:
    def __init__(self, effort_fl = 0.0, effort_fr = 0.0, effort_bl = 0.0, effort_br = 0.0):
        self.effort_fl = effort_fl
        self.effort_fr = effort_fr
        self.effort_bl = effort_bl
        self.effort_br = effort_br

    def __add__(self, o):
        fl = self.getEffortFL() + o.getEffortFL()
        fr = self.getEffortFR() + o.getEffortFR()
        bl = self.getEffortBL() + o.getEffortBL()
        br = self.getEffortBR() + o.getEffortBR()
        return PlatformEffort(fl, fr, bl, br)

    def __str__(self):
        return "(fr: {}, fl: {}, bl: {}, br{})".format(self.effort_fr, self.effort_fl, self.effort_bl, self.effort_br)
    
    def getEffortFL(self):
        return self.effort_fl
    
    def getEffortFR(self):
        return self.effort_fr
    
    def getEffortBL(self):
        return self.effort_bl
    
    def getEffortBR(self):
        return self.effort_br
    
    def normalize(self):
        # scale all efforts proportionally if necessary so they are within [-1, 1]
        max_val = max(abs(self.effort_fl), abs(self.effort_fr), abs(self.effort_bl), abs(self.effort_br))
        if max_val > 1.0:
            self.effort_fl = self.effort_fl / max_val
            self.effort_fr = self.effort_fr / max_val
            self.effort_bl = self.effort_bl / max_val
            self.effort_br = self.effort_br / max_val
            
    def clamp(self):
        #clamp all values to within [-1, 1]
        clamp_effort(self.effort_fl)
        clamp_effort(self.effort_fr)
        clamp_effort(self.effort_bl)
        clamp_effort(self.effort_br)
        
    def clamp_effort(self, effort):
        return max(-1.0, min(1.0, effort))

