import numpy as np
import cv2
import mediapipe as mp
import time
from PIL import Image
import matplotlib.pyplot as plt
import os
from pynput.keyboard import Key, Listener

p = os.path.abspath('file.txt ')



cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def make_dot_screen():
    pass
                        

while True:

            success, img = cap.read()
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(imgRGB) 
            if results.multi_hand_landmarks:
                for handLms in results.multi_hand_landmarks:
                    #pointsX =[]#создание массива
                    #pointsY =[]#создание массива
                    for id, lm in enumerate(handLms.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x*w), int(lm.y*h)
                        print(cx, cy)
                        #     with open(p, 'a' ) as file:
                        #         file.writelines(str(cx)) 
                        #         print(str(cx))

                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
      
            # def on_press(key):
            #     print('{0} pressed'.format(key))

            # def on_release(key):
            #     print('{0} release'.format(key))

            #     if key == Key.space:
            #         make_dot_screen()

            cv2.imshow("", img)
            cv2.waitKey(1)
            
            # with Listener(on_press=on_press, on_release=on_release) as listener:
            #     listener.join()           

