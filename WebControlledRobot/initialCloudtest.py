
import time
import requests

'''This part is working with  the cloud'''
link = "https://morning-brushlands-7219.herokuapp.com/"
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

'''Run this infinitely'''
while True:
val = checkCommandExists()
if val != None:
	val = getSerialCommand(val)
	print val
	
	 

