import pyrebase
import platform
import os
import glob
import time
import cv2
#import RPi.GPIO as GPIO 

selfID="Car1" ##this is the dummy for the self's Number Plate unique ID

config={        #fill according to your firebase database
    "apiKey": " AIzaSyAPumd637Cml2lncPQWARhnE0oei_AsyeU ",
    "authDomain": "overtake-5888b.firebaseapp.com",
    "databaseURL": "https://overtake-5888b.firebaseio.com/",
    "storageBucket": "overtake-5888b.appspot.com"
}
firebase =pyrebase.initialize_app(config)
db=firebase.database()
#For turning LED Green/Red On or Off
'''GPIO.setmode(GPIO.BOARD)
mypinG = 11
mypinR = 12
GPIO.setup(mypinG, GPIO.OUT, initial = 0)
GPIO.setup(mypinR, GPIO.OUT, initial = 0)'''
overtake=1

car_cascade = cv2.CascadeClassifier('trial2.xml')
vc = cv2.VideoCapture('C:\\Users\\asd\\Desktop\\HashHacks3.0\\006.mp4')

if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False
c1=250
area=0
pos=0
r1=0
center=500
def carDetect():
    rval, frame = vc.read()
    frameY, frameX, frameD = frame.shape
    # frame = cv2.resize(frame,(int(frameX/2), int(frameY/2)))
    frameY, frameX, frameD = frame.shape
    #print(frameX, frameY) 
    frame = frame[(int)(frameY*0.40):(int)(frameY*0.90), (int)(frameX*0.45):(int)(frameX*0.45)+(int)(frameX*0.9)]
    frameY, frameX, frameD = frame.shape
    # frame = cv2.resize(frame, (int(frameX*1.5), int(frameY*1.5)))
    # frame = cv2.resize(frame,(640, 300))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    cars = car_cascade.detectMultiScale(gray,1.2, 5)
    ncars = 0
    for (x,y,w,h) in cars:
        area=w*h
        pos=x+(h/2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
        ncars = ncars + 1
    return(ncars)
    # show result
    #cv2.imshow("Result",frame)
    #print ncars
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

def stream_handler(message):
    print(message["data"])
    overtake=int(message["data"])
    if(overtake==0):
        #GPIO.output(mypinG, 1)
        #GPIO.output(mypinR, 0)
        print("Overtake")
    else:
        #GPIO.output(mypinG, 0)
        #GPIO.output(mypinR, 1)
        print("Dont Overtake")
def getPlateID():
    ###Here goes the detction code for Number Plate
    ###Number Plate Detection Code Returns a number- Plate which is the unique id for the detected car
    return 'Car2'
def PlatePresent():
    if(getPlateID!=''):
        return 1
    else:
        return 0
#print("Listening to stream")
#my_stream = db.child("Cars").child(Plate).stream(stream_handler)
PlateTemp='Temp'
while(True):
    ######
    #checkForPlate
    ######
    if(PlatePresent()!=0):
        Plate=getPlateID();
        if(Plate!=PlateTemp):
            PlateTemp=Plate
            my_stream = db.child("Cars").child(Plate).stream(stream_handler)
    #######
    #Check for car in front
    #######
    carPresent=carDetect()
    if(carPresent==0):
        db.child("Cars").child(selfID).set('0')
        print("Updating 0")
    else:
        db.child("Cars").child(selfID).set('1')
        print("Updating 1")
