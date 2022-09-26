#basic python support for pi-bci systems
#this program will determine what to do with each pin so it can be modified to support non-standard derivative designs. 
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
#Example: How to read in GPIO input on pin 20
#GPIO.setup(20, GPIO.IN)

