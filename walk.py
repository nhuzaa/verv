import time

from servo import servo

eyepin = 25
# Left leg
lHipRot = 22
lHip = 27
lKnee = 17
lBase = 4

# Right leg
rHipRot = 6
rHip = 13
rKnee = 19
rBase = 26

lHipServo = servo(lHip, "lHip")
lKneeServo = servo(lKnee, "lKnee")
lBaseServo = servo(lBase, "lBase")

rBaseServo = servo(rBase, "rBase")

lHipServo.set(90)
lKneeServo.set(90)
lBaseServo.set(90)

rBaseServo.set(90)

while True:
    # lHipServo.slowset(0)
    # lKneeServo.slowset(180)
    lBaseServo.slowset(0)
    rBaseServo.slowset(0)
    time.sleep(1)
    # lHipServo.slowset(180)
    # lKneeServo.slowset(0)
    lBaseServo.slowset(90)
    rBaseServo.slowset(90)
    time.sleep(1)
