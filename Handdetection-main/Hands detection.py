from xml.etree.ElementPath import prepare_self
import numpy as np
import cv2
import mediapipe as mp
import time
from PIL import Image
import matplotlib.pyplot as plt
import os
from pynput.keyboard import Key, Listener
import keyboard

p = os.path.abspath('file.txt ')

key = 'space'

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

#def make_dot_screen():
    #pass
                        

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
                    if keyboard.is_pressed(key):
                        with open("file.txt", "a") as file:
                            if id == 0:
                                file.write(f"{str(cx)},{str(cy)} ")
                            else:
                                file.write(f"{str(cx)},{str(cy)} ")
                
                if keyboard.is_pressed(key):
                    with open("file.txt", "a") as file:
                            file.write(f"\n")
                

                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

                cv2.imshow("", img)
                cv2.waitKey(1)

#            with open(p, 'a' ) as file:
 #               file.writelines(str(cx)) 
        #print(str(cx))

#            def on_press(key):
#                    print('{0} pressed'.format(key))
#
 #           def on_release(key):
  #                  print('{0} release'.format(key))
#
 #           if key == Key.space:
  #              make_dot_screen()
#
          

   #         
    #        with Listener(on_press=on_press, on_release=on_release) as listener:
     #            listener.join()   
