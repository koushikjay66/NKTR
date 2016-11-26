import RPi.GPIO as GPIO
import os
import MFRC522
import signal
from subprocess import *
from time import sleep, strftime
from datetime import datetime
from Adafruit_CharLCD import Adafruit_CharLCD
from db_helper import *
from ip import *
from buzzer import *
from led import *
continue_reading = True



# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

#These codes are for RFID


# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()
lcd = Adafruit_CharLCD()
lcd.begin(16, 2)

def lcdmod(displayText, time, boolean):
    lcd.clear()
    lcd.setCursor(0, 0)  # rows start at 0
    
    lcd.message(displayText)

    if(time!=1):
        sleep(time)
        lcd.clear()



#This Line is for Hardware Reboot
GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


# Now the Actual Program Starts .
# TO give feedback to the user we now Lid the LED
GPIO.setup(36,GPIO.OUT)
GPIO.output(36, True)
#End of Lighting the LED


# Welcome message
print "Welcome to Our Project "
lcdmod("Welcome to Our \nProject ", 1, False)


#It is time to get the Course ID and Section From Server
details=getCourse()
courseID=details[0:6]
section =details[7:]

#Rest the Inroom People Count
resetCount()
lcdmod("Course: "+courseID+"\nSection:"+section, 5, True)

while continue_reading:
    lcdmod(getRoomtatus(), 1, True)

    #If user has pushed the Button I need to Reboot The RPI
    if(GPIO.input(7)==1):
        lcdmod("Rebooting in \n2 seconds.....", 3, True)
        lcd.clear()
        os.system('sudo reboot')
    #End of Statement if User has pushed Reboot Button

        
    # Scan for cards
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print
        "Card detected"

    # Get the UID of the card
    (status, uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
      stdid = str(uid[0]) + "." + str(uid[1]) + "." + str(uid[2]) + "." + str(uid[3])
      print "id = "+stdid+"\n"

     #When Found Card I want to FeedBack via Buzzer
      foundCard()
     #Now as I have got the id from RFID in stdid We can query to get the Name.
      lcdmod("ID Read\nWait...)", 1, False)
      attendance(stdid,courseID, section)
      lcdmod(getName(stdid), 2, False)
      



