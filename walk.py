import time

from servo import servo

eyepin = 25
# Left leg
lHipRot = 4
lHip = 27
lKnee = 17
lBase = 22

lHipServo = servo(lHip, "lHip")
lKneeServo = servo(lKnee, "lKnee")
lHipRotServo = servo(lHipRot, "lHipRot")

lHipServo.set(90)
lKneeServo.set(90)
lHipRotServo.set(90)
while True:
    lHipServo.slowset(0)
    lKneeServo.slowset(180)
    lHipRotServo.slowset(20)
    time.sleep(1)
    lHipServo.slowset(180)
    lKneeServo.slowset(0)
    lHipRotServo.slowset(80)
    time.sleep(1)
