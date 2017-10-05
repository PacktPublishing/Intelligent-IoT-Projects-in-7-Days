import numpy as np
import cv2


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

img = cv2.imread('IMG_FACE.JPG')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)

print "Number of faces detected: " + str(faces.shape[0])

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
