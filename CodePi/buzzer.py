import RPi.GPIO as GPIO
import time

def setUpBuzzer():
    GPIO.setup(12,GPIO.OUT)

def foundCard():
    setUpBuzzer()
    GPIO.output(12, True)
    time.sleep(0.25)
    GPIO.output(12, False)
    GPIO.cleanup(12)
