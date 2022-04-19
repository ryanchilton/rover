import time
import math
from mecanum_platform import MecanumPlatform

platform = Platform()

for i in range (1,36):
    platform.translate(angle_rad = i*10 * math.pi/180.0, effort = 0.6)
    time.sleep(0.2)
platform.stop()

# platform.rotate(effort = 0.4)
# time.sleep(3)
# platform.rotate(effort = -0.4)
# time.sleep(3)

# platform.stop()
# time.sleep(2)

# platform.translate(angle_rad = 45 * math.pi/180.0, effort = 0.5)
# time.sleep(2)
# platform.translate(angle_rad = 180 * math.pi/180.0, effort = 0.5)
# time.sleep(3)
# platform.translate(angle_rad = 315 * math.pi/180.0, effort = 0.5)
# time.sleep(4)
# platform.translate(angle_rad = 180 * math.pi/180.0, effort = 0.5)
# time.sleep(3)
# platform.translate(angle_rad = 45 * math.pi/180.0, effort = 0.5)
# time.sleep(2)


platform.stop()

