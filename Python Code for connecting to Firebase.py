import pyrebase
import platform
import os
import glob
import time

config={        #fill according to your firebase database
    "apiKey": " AIzaSyAPumd637Cml2lncPQWARhnE0oei_AsyeU ",
    "authDomain": "overtake-5888b.firebaseapp.com",
    "databaseURL": "https://overtake-5888b.firebaseio.com/",
    "storageBucket": "overtake-5888b.appspot.com"
}
firebase =pyrebase.initialize_app(config)
db=firebase.database()
groups=db.child("Groups").get()
print(groups.val())



'''def uploadMess(tuSun,yeSun):
    db.child(tuSun).update(yeSun)
    

my_stream = db.child("database1").child(ting).child("Message").stream(stream_handler)
while True:          
        data1=''
        forQuit=''
        data=''
        while 1:
                try:
                    dataone=({'Lat':Lat,'Long':Long,'Alt':Alt,'Speed':Speed})
                    db.child("database1").child(ting).child("Location").update(dataone)       
'''
