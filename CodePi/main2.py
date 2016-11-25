import RPi.GPIO as GPIO
import MFRC522
import signal
from subprocess import *
from time import sleep, strftime
from datetime import datetime
from Adafruit_CharLCD import Adafruit_CharLCD
#from database_connect import insertStudent
from db_helper import *
from ip import *

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
        
    
    #if boolean==True:
    #   lcd.clear()




# Welcome message
print "Welcome to Our Project "
lcdmod("Welcome to Our \nProject ", 1, False)
#It is time to get the Course ID and Section From Server
details=getCourse()
courseID=details[0:6]
section =details[7:]
resetCount()
lcdmod("Course: "+courseID+"\nSection:"+section, 5, True)

while continue_reading:
    lcdmod(getRoomtatus(), 1, True)
    
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
      
     #Now as I have got the id from RFID in stdid We can query to get the Name.
      lcdmod("ID Read\nWait...)", 1, False)
      lcdmod(getName(stdid), 2, False)
      



