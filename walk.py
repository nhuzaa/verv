import time

from servo import servo

eyepin = 25
# Left leg
lHipRot = 4
lHip = 17
lKnee = 27
lBase = 22

lHipServo = servo(lHip)

while True:
    lHipServo.set(0)
    time.sleep(1)
    lHipServo.set(180)
    time.sleep(1)
