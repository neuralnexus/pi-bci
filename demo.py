#basic python support for pi-bci systems
#this program will determine what to do with each pin so it can be modified to support non-standard derivative designs. 
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
