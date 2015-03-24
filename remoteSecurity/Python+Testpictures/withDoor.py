def captureImage(initialName,finalName,timeInterval):
        camera.capture(initialName+'.jpg')
        time.sleep(timeInterval)
        fileName(initialName+'.jpg',finalName) #This function is going to add the extension to finalName
'''The image being captured here will be stored in the same folder as the code '''
###################################### Input from PIR sensor and various values ###############################
''' Define input pins '''
pin1 = 4
pin2 = 7
''' GPIO Setup '''
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin1,GPIO.IN) #Define input
GPIO.setup(pin2,GPIO.OUT)#Define output
time.sleep(5)
################# Function for motor movement etc #############################
def openDoorY():
        #gpio high signal
def openDoorN():
        #gpio low signal
#################### Function for receiving response from the webpage ###########
'''This part is working with  the cloud'''
link = "https://sheltered-inlet-1735.herokuapp.com/command"
def checkCommand():
        r = requests.get(link)
        curValue = r.text
        if curValue == "none":
                return None
        else:
                if "Y" in curValue:
                        #Open the door
                        openDoorY()
                if "N" in curValue:
                        #Close the door
                        openDoorN()
while True:
        #print (GPIO.input(4))
        if (GPIO.input(4)):
                captureImage("newName","intruder", 0.5)
                print "Intruder captured"
                checkCommand()

