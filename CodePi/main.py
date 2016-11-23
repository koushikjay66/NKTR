import RPi.GPIO as GPIO
import MFRC522
import signal
from subprocess import *
from time import sleep, strftime
from datetime import datetime
from Adafruit_CharLCD import Adafruit_CharLCD
from database_connect import insertStudent

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


while continue_reading:

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
      #get corresponding student name
      found=False

      name="invalid id"
      with open("info.txt") as f:
         line=f.readline()
         if stdid not in line:
             print "not ok"
             #continue
         else:
             name=line[(line.index(' ')+1):]
             
             found=True
             
             

      
      insertStudent("select * from counter where rfid=`0`")
        
      lcdmod(name, 2, False)



