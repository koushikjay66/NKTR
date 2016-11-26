import time

def setUpChor():
    GPIO.setup(11,GPIO.OUT)

def chor():
    setUpChor()
    GPIO.output(11, True)
    time.sleep(2)
    GPIO.output(11, False)
    GPIO.cleanup(11)


