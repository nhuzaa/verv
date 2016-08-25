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

lHipRotServo.set(90)
rHipRotServo.set(90)
while True:

    # # center
    # x = input("Right Base Servo")
    # print(int(x))
    # rBaseServo.set(int(x))
    # time.sleep(1)
    # x = input("left Base Servo")
    # print(int(x))
    # lBaseServo.set(int(x))
    # time.sleep(1)

    # Preparation of Right leg up
    # lean left
    rBaseServo.slowset(180)
    time.sleep(1)
    lBaseServo.slowset(180)
    time.sleep(1)

    # Right UP
    rKneeServo.slowset(180)
    time.sleep(1)
    rHipServo.slowset(0)
    time.sleep(1)

    # center
    rBaseServo.slowset(120)
    time.sleep(1)
    lBaseServo.slowset(160)
    time.sleep(1)

    # Right Down
    rKneeServo.slowset(90)
    time.sleep(1)
    rHipServo.slowset(90)
    time.sleep(1)

    # Prepartion for Left Leg up
    # Lean Right
    rBaseServo.slowset(40)
    time.sleep(1)
    lBaseServo.slowset(30)
    time.sleep(1)

    # left UP
    lKneeServo.slowset(0)
    time.sleep(1)
    lHipServo.slowset(180)
    time.sleep(1)

    # center
    rBaseServo.slowset(120)
    time.sleep(1)
    lBaseServo.slowset(160)
    time.sleep(1)

    # Left Down
    lKneeServo.slowset(90)
    time.sleep(1)
    lHipServo.set(90)
    time.sleep(1)
