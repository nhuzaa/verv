import time

from servo import servo

eyepin = 25
# Left leg
lHipRot = 4
lHip = 27
lKnee = 17
lBase = 22

lHipServo = servo(lHip)
lKneeServo = servo(lKnee)
while True:
    lHipServo.slowset(0)
    lKneeServo.slowset(180)
    time.sleep(1)
    lHipServo.slowset(180)
    lKneeServo.slowset(0)
    time.sleep(1)
