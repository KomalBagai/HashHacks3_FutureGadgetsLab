import pyrebase
import platform
import os
import glob
import time


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
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BOARD)
mypinG = 11
mypinR = 12
GPIO.setup(mypinG, GPIO.OUT, initial = 0)
GPIO.setup(mypinR, GPIO.OUT, initial = 0)
overtake=1

def uploadMess(tuSun,yeSun):
    db.child("Groups").child(tuSun).update(yeSun)
def stream_handler(message):
    print(message["data"])
    overtake=int(message["data"])
    if(overtake==0):
        GPIO.output(mypinG, 1)
        GPIO.output(mypinR, 0)
        print("Overtake")
    else:
        GPIO.output(mypinG, 0)
        GPIO.output(mypinR, 1)
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
