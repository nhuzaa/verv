import time

import RPi.GPIO as GPIO

from servo import servo

eyepin = 25
# Left leg
lHipRot = 4
lHip = 17
lKnee = 27
lBase = 22

slHip = servo()
