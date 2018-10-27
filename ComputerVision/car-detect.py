#! /usr/bin/python

import cv2

car_cascade = cv2.CascadeClassifier('trainedmodel-car.xml')
vc = cv2.VideoCapture('video-4.mp4')

if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False
c1=250
area=0
pos=0
r1=0
center=500
while True:
    
    rval, frame = vc.read()
    frameY, frameX, frameD = frame.shape
    # frame = cv2.resize(frame,(int(frameX/2), int(frameY/2)))
    frameY, frameX, frameD = frame.shape
    print(frameX, frameY) 
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

    # show result
    cv2.imshow("Result",frame)
    #print ncars
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

vc.release()
cv2.destroyAllWindows()
