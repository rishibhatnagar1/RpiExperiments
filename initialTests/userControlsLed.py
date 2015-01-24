import RPi.GPIO as GPIO
import time
#pins intended for use
pin = 17

#GPIO setup

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Pins Initialization
GPIO.setup(pin,GPIO.OUT)

#Defining various functions for use
def on ():
        GPIO.output(pin,GPIO.HIGH)
def off():
        GPIO.output(pin,GPIO.LOW)
def ledStatus(val):
        if "on" in val or "ON" in val or "On" in val or "oN" in val:
                on()
        elif "off" in val or "OFF" in val or "OfF" in val :
                off()
        else:
                print "Enter something valid bro"
while True:
	val = raw_input ("Input On/Off here to test the LEDs: ")
	if (val!=NONE):      
        	ledStatus(val)
	#You could do a GPIO cleanup here using GPIO.cleanup , in an else condition ofcourse.
	



