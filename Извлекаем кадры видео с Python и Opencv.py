import cv2
import numpy as np


# открываем встроенную веб камеру
cap = cv2.VideoCapture(0)
# или видеозапись
# cap = cv2.VideoCapture("путь/record.mp4", cv2.CAP_DSHOW)


# устанавливаем счетчик
counter=0

# запускаем бесконечный цикл и проверяем статус камеры
while cap.isOpened():
   
    # читаем кадры с записи или камеры в frame
    _, frame = cap.read()
   
    # переводим кадр в черно-белую градацию
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # создаем функцию классификатор и сохраняем ее в переменной
    face_cascade = cv2.CascadeClassifier("C:\Users\m.Toporkov\Downloads\Handdetection-main\Handdetection-main/haarcascade_frontalface_default.xml")
    # вызываем метод с параметром в виде кадра gray
    # метод вернет список найднных областей
    faces = face_cascade.detectMultiScale(gray)

    # выделяем на кадре эти области прямоугольником
    for x, y, width, height in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)

   
     # вырезаем и сохраняем  найденные объекты
     # в папку detected_from_video_screen. Точка перед ней указывает на текущий каталог
    for x, y, width, height in faces:
        crop_img = frame[y:y + height, x:x + width]
        cv2.imwrite("./detected_from_video_screen/face_{0}.jpg".format(counter), crop_img)
        counter = counter+1

    cv2.imshow("frame", frame)
    if cv2.waitKey(40) == 27:
      break


cap.release()
cv2.destroyAllWindows()
print('done')