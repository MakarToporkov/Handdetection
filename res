import numpy as np
import cv2
import mediapipe as mp
import time
from PIL import Image
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)


fps = 20.0
image_size = (640,480)
video_file = 'res.avi'


out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'XVID'), fps, image_size)
i = 0;
while True:
    ret, frame = cap.read()
    out.write(frame)
    time.sleep(0.05)
    i = i + 1
    if i > 1000:
        break;

cap.release()
cv2.destroyAllWindows()


'''import cv2 as cv
 

 # Скриншот изображения
def cutVideo():
    i = 0
    video = cv.VideoCapture ('video.avi') # читать видеофайл
    while(True):
        ret,frame = video.read()
        cv.imshow('video',frame)
        c = cv.waitKey(50)
        if c == 27:
            break
        i=i+1
        if i%5==0:
            cv.imwrite('D:\\save\\'+str(i)+'.png',frame)
 
 
cutVideo()
cv.destroyAllWindows()'''
                


