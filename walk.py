import time

from servo import servo

eyepin = 25

# Left leg
lHipRot = 6
lHip = 13
lKnee = 19
lBase = 26

# Right leg
rHipRot = 22
rHip = 27
rKnee = 17
rBase = 4

lHipRotServo = servo(lHipRot, "lHipRot")
lHipServo = servo(lHip, "lHip")
lKneeServo = servo(lKnee, "lKnee")
lBaseServo = servo(lBase, "lBase")

rHipRotServo = servo(rHipRot, "rHipRot")
rHipServo = servo(rHip, "rHip")
rKneeServo = servo(rKnee, "rKnee")
rBaseServo = servo(rBase, "rBase")

lHipRotServo.set(70)
rHipRotServo.set(70)
while True:

    # center
    x = input("Right Base Servo")
    rBaseServo.set(x)
    time.sleep(1)
    x = input("left Base Servo")
    lBaseServo.set(x)
    time.sleep(1)
    #
    # # Preparation of Right leg up
    # # lean left
    # rBaseServo.set(160)
    # time.sleep(1)
    # lBaseServo.set(130)
    # time.sleep(1)
    #
    # # Right UP
    # rKneeServo.set(180)
    # time.sleep(1)
    # rHipServo.set(0)
    # time.sleep(1)
    #
    # # center
    # rBaseServo.set(90)
    # time.sleep(1)
    # lBaseServo.set(60)
    # time.sleep(1)
    #
    # # Right Down
    # rKneeServo.set(90)
    # time.sleep(1)
    # rHipServo.set(90)
    # time.sleep(1)
    #
    # # Prepartion for Left Leg up
    # # Lean Right
    # rBaseServo.set(20)
    # time.sleep(1)
    # lBaseServo.set(0)
    # time.sleep(1)
    #
    # # left UP
    # lKneeServo.set(0)
    # time.sleep(1)
    # lHipServo.set(180)
    # time.sleep(1)
    #
    # # center
    # rBaseServo.set(90)
    # time.sleep(1)
    # lBaseServo.set(60)
    # time.sleep(1)
    #
    # # Left Down
    # lKneeServo.set(90)
    # time.sleep(1)
    # lHipServo.set(90)
    # time.sleep(1)
