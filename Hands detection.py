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
            pointsX =[]#создание массива
            pointsY =[]#создание массива
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                pointsX.append(cx)
                pointsY.append(cy)
        
            # minX = min(pointsX) - int((min(pointsX))*0.12)попытка отступов
            # minY = min(pointsY) - int((min(pointsY))*0.08)попытка отступов
            # maxX = max(pointsX) + int((max(pointsX))*0.03)попытка отступов
            # maxY = max(pointsY) + int((max(pointsY))*0.01)попытка отступов
            minX = min(pointsX) #создание переменной для нахождения минимального значения массива по оси Х
            minY = min(pointsY) #создание переменной для нахождения минимального значения массива по оси Y
            maxX = max(pointsX) #создание переменной для нахождения максимального значения массива по оси Х
            maxY = max(pointsY) #создание переменной для нахождения максимаоьного значения массива по оси Y

            cv2.rectangle(img, ( minX, minY), (maxX, maxY), (255, 0 ,0))#построение прямоугольника по минимальным и максимальным точкам
                

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


    cv2.imshow("Image", img)
    cv2.waitKey(1)
                

        

    








"""for i in range(1, 192):
  if 'zip' not in imgs_for_convertation[i] and 'json' not in imgs_for_convertation[i]:
    image_file = np.asarray(Image.open(os.path.join(train_data_dir, imgs_for_convertation[i])))
    image_file = np.resize(image_file, 224*224*1)
    #print(i)
    images[i] = image_file"""



