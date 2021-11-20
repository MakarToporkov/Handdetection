import numpy as np
import cv2
import mediapipe as mp
import time
from PIL import Image
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            pointsX =[]
            pointsY =[]
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                pointsX.append(cx)
                pointsY.append(cy)
                #print(id, cx, cy)
                #cv2.circle(img, (cx, cy), 7, (255, 0, 0), cv2.FILLED)
            minX = min(pointsX) - (min(pointsX))*0.01
            minY = min(pointsY) - (min(pointsY))*0.01
            maxX = max(pointsX) + (max(pointsX))*0.01
            maxY = max(pointsY) + (max(pointsY))*0.01
            # X1 = minX - minX * 0.1
            # Y1 = minY - minY * 0.1
            # X2 = maxX + maxX * 0.1
            # Y2 = maxY + maxY * 0.1
            # cv2.rectangle(img, ( X1, Y1), (X2, Y2), (255, 0 ,0))
            cv2.rectangle(img, ( minX, minY), (maxX, maxY), (255, 0 ,0))
                

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
                

        

    








"""for i in range(1, 192):
  if 'zip' not in imgs_for_convertation[i] and 'json' not in imgs_for_convertation[i]:
    image_file = np.asarray(Image.open(os.path.join(train_data_dir, imgs_for_convertation[i])))
    image_file = np.resize(image_file, 224*224*1)
    #print(i)
    images[i] = image_file"""



