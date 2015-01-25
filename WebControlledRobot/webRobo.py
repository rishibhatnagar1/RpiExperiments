import RPi.GPIO as GPIO
import time
import requests

#Initialize the GPIOs
GPIO.setmode(GPIO.BCM) #This is to name GPIOS
GPIO.setwarning(False) 
p1 = GPIO17
p2 = GPIO27
#Initialize the pins to their INPUT/OUPUT nature
#GPIO.setup(pinNumber,GPIO.IN/OUT)
GPIO.setup(p1,GPIO.OUT) 
GPIO.setup(p2,GPIO.OUT)

'''This part is working with  the cloud'''
link = ""
def checkCommandExists():
	r = requests.get(link)
	curValue = r.text
	if curValue == "none":
		return None
	else:
		return curValue

def getSerialCommand(cmd):
	if "f" in cmd :
		return "f"
	elif "b" in cmd:
		return "b"
	elif "r" in cmd:
		return "r"
	elif "l" in cmd:
		return "l"
	elif "s" in cmd :
		return "s"
'''This part here is to work with your application, this case it is a wheelchair '''
def moveForward():
	GPIO.output(p1,GPIO.HIGH)#Both the pins will be high, moving forward
	GPIO.output(p2,GPIO.HIGH)
	print "forward"
def stop():
	GPIO.output(p1,GPIO.LOW)#Both wheels come to halt
	GPIO.output(p1,GPIO.LOW)
	print "stop"
def moveRight():
	GPIO.output(p1,GPIO.HIGH)#One moves, other doesn't
	time.sleep(0.5)
	GPIO.output(p2,GPIO.LOW)
	print "Right"
def moveLeft():
	GPIO.output(p2,GPIO.HIGH)#same logic as above
	time.sleep(0.5)
	GPIO.output(p1,GPIO.LOW)
	print "Left"
def moveBackward():
	GPIO.output(p1,GPIO.HIGH)#move in the same direction and 180degree turn
	time.sleep(2) #Need to test this

#Function to decide the right movement more can be added using the same logic
def setMotionStatus(inpVal):
	if "f" in inpVal:
		moveForward()
	elif "s" in inpVal:
		stop()
	elif "b" in inpVal:
		moveBackward()
	elif "l" in inpVal:
		moveLeft()
	elif "r" in inpval:
		moveRight()
	else:
		stop()
		GPIO.flush() #Keep the GPIOs clean

'''Run this infinitely'''
while True:
val = checkCommandExists()
if val != None:
	val = getSerialCommand(val)
	print val
	setMotionStatus(val)
	 

