# ! /usr/bin/python

import cv2
import numpy as np

plate_cascade = cv2.CascadeClassifier('numberplate.xml')#cas1
vid = '/Users/ishani/AnacondaProjects/HashHacks3_FutureGadgetsLab/Data/video-1.MOV'
vc = cv2.VideoCapture(vid)

if vc.isOpened():
    rval , frame = vc.read()
else:
    rval = False

while True:
     rval, frame = vc.read()
     frameY, frameX, frameD = frame.shape
     frame = cv2.resize(frame,(3*frameX, 3*frameY))
    # #   frames = frames[c1:c1+170,r1:r1+510]

     frameY, frameX, frameD = frame.shape
     frame = frame[(int)(frameY*0.6):(int)(frameY*0.8), (int)(frameX*0.44):(int)(frameX*0.6)]
     frameY, frameX, frameD = frame.shape

     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

     kernel = np.ones((5,5), np.uint8)
     gray = cv2.erode(frame, kernel, iterations=1)
     gray = cv2.dilate(frame, kernel, iterations=1)
     cars = plate_cascade.detectMultiScale(frame,scaleFactor = 1.2,minNeighbors = 2,flags = cv2.CASCADE_SCALE_IMAGE)


     # ncars = 0
     for (x,y,w,h) in cars:

        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
      
     cv2.imshow("Result",frame)

     cv2.waitKey(0)

vc.release()
cv2.destroyAllWindows()
