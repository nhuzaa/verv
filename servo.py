import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


def map(angle):

    percent = angle / 180
    p = percent * (10.5 - 4.5)
    p = p + 4.5
    return p


class servo:

    angle = 90
    pulse = 7.5
    s = None
    pin = None

    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(pin, GPIO.OUT)
        self.s = GPIO.PWM(pin, 50)
        self.s.start(map(self.angle))

    # def up(self):
    #     if(self.angle <= 10.5 and self.angle >= 4.5):
    #         self.angle = self.angle + 0.25
    #         print("Yservo " + str(self.angle))
    #         pY.ChangeDutyCycle(self.angle)
    #         time.sleep(0.02)
    #     else:
    #         self.limit()
    #
    # def down(self):
    #     if(self.angle <= 10.5 and self.angle >= 4.5):
    #         self.angle = self.angle - 0.25
    #         print("Yservo " + str(self.angle))
    #         pY.ChangeDutyCycle(self.angle)
    #         time.sleep(0.02)
    #     else:
    #         self.limit()
    def slowset(self, angle):
        if(self.angle < angle):
            for x in range(self.angle, angle + 1):
                self.s.ChangeDutyCycle(map(x))
                print("Angle" + str(x))
                time.sleep(0.022)
            self.angle = angle
        else:
            for x in range(self.angle, angle + 1, -1):
                self.s.ChangeDutyCycle(map(x))
                print("Angle" + str(x))
                time.sleep(0.022)
            self.angle = angle

    def set(self, angle):
        self.s.ChangeDutyCycle(map(angle))
        print("Angle" + str(angle))
        self.angle = angle

    def limit(self):
        if(self.angle > 180):
            self.angle = 180
        elif(self.angle < 0):
            self.angle = 0
