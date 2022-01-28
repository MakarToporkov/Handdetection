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

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")
out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'XVID'), fps, image_size)
i = 0;
while True:
    ret, frame = cap.read()
    out.write(frame)
    time.sleep(0.0)
    i = i + 1
    if i > 1000:
        break;

cap.release()
cv2.destroyAllWindows()

print("Successfully saved")
                
