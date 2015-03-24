''' The code has been written by Rishi Gaurav Bhatanagar (@rishigb) for a #stilllife project (with @justusbruns) , all code written and tested
    with Pi B/B+, in association with Workbench Projects'''
import picamera
import requests
import time
import RPi.GPIO as GPIO
''' The following code will be used to send a picture '''
url_image = 'https://sheltered-inlet-1735.herokuapp.com/pagemulti'
camera = picamera.PiCamera()
camera.resolution =(640,460)

####################################### Image Posting #######################################################
def fileName (cur_name,post_name):
    files ={post_name:open(cur_name,'rb')}
        r = requests.post(url_image,files=files)
        if (r.status_code) ==200:
            print "Posted"
        else:
            print r.status_code

####################################Capturing Image ##########################################################
def captureImage(initialName,finalName,timeInterval):
    camera.capture(initialName+'.jpg')
        time.sleep(timeInterval)
        fileName(initialName+'.jpg',finalName) #This function is going to add the extension to finalName
'''The image being captured here will be stored in the same folder as the code '''
###################################### Input from PIR sensor and various values ###############################
''' Define input pins '''
pin = 4
''' GPIO Setup '''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin,GPIO.IN) #Define input
time.sleep(5)

while True:
    #print (GPIO.input(4))
    if (GPIO.input(4)):
        captureImage("newName","intruder", 0.5)

'''To view the image capture go the following link: https://sheltered-inlet-1735.herokuapp.com/images?value=intruder.jpg '''