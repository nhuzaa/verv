import time
from multiprocessing import Process

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

# Right Hand
rshld = 16
relb = 12

# Left Hand
lshld = 21
lelb = 20


rshldServo = servo(rshld, "rshld")
relbServo = servo(relb, "relb")

lshldServo = servo(lshld, "lshld")
lelbServo = servo(lelb, "lelb")

lHipRotServo = servo(lHipRot, "lHipRot")
lHipServo = servo(lHip, "lHip")
lKneeServo = servo(lKnee, "lKnee")
lBaseServo = servo(lBase, "lBase")

rHipRotServo = servo(rHipRot, "rHipRot")
rHipServo = servo(rHip, "rHip")
rKneeServo = servo(rKnee, "rKnee")
rBaseServo = servo(rBase, "rBase")


def righthandMotion():

    rshldServo.slowset(20)
    relbServo.slowset(20)
    rshldServo.slowset(170)
    relbServo.slowset(170)


def lefthandMotion():

    lshldServo.slowset(170)
    lelbServo.slowset(170)
    lshldServo.slowset(20)
    lelbServo.slowset(20)


def legMotion():

    lHipRotServo.set(90)
    rHipRotServo.set(100)

    # # center
    # x = input("rBaseServo Base Servo")
    # print(int(x))
    # rBaseServo.set(int(x))
    # time.sleep(1)
    # x = input("left Base Servo")
    # print(int(x))
    # lBaseServo.set(int(x))
    # time.sleep(1)

    #
    # Preparation of Right leg up
    # lean left
    rBaseServo.slowset(170)
    lBaseServo.slowset(170)

    # Right UP
    rKneeServo.slowset(180)
    rHipServo.slowset(0)

    # center
    rBaseServo.slowset(150)

    lBaseServo.slowset(130)

    # Right Down
    rKneeServo.slowset(90)

    rHipServo.slowset(90)

    # Prepartion for Left Leg up
    # Lean Right
    rBaseServo.slowset(0)

    lBaseServo.slowset(0)

    # left UP
    lKneeServo.slowset(0)

    lHipServo.slowset(180)

    # center
    rBaseServo.slowset(150)

    lBaseServo.slowset(130)

    # Left Down
    lKneeServo.slowset(90)

    lHipServo.set(90)

if __name__ == '__main__':
    # p1 = Process(target=righthandMotion)
    # p1.start()
    # p2 = Process(target=lefthandMotion)
    # p2.start()
    # p3 = Process(target=legMotion)
    # p3.start()
    while True:
        lefthandMotion()
        righthandMotion()
        legMotion()
