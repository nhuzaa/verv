
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


class servo:

    angle = 90
    pulse = 7.5
    s = None

    def __init__(self, pin):
        GPIO.setup(pin, GPIO.OUT)
        s = GPIO.PWM(pinout1, 50)
        s.start(map(self.angle))

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

    def set(self, angle):

        pY.ChangeDutyCycle(map(angle))
        print("Angle" + str(angle))

    def map(self, angle):

        percent = angle / 180
        p = percent * (10.5 - 4.5)
        p = p + 4.5
        self.pulse = p
        return p

    def limit(self):
        if(self.angle > 180):
            self.angle = 180
        elif(self.angle < 0):
            self.angle = 0
