import math
import time
import webbrowser

import cv2
from cvzone.ClassificationModule import Classifier
import numpy as np
import urllib.request

from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

classifier = Classifier("Model/keras_model.h5","Model/labels.txt")


offset = 20
imgSize = 224
labels = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X'
          ,'Y','Z','del','space']
print(len(labels))
s = ""
last_prediction_time =0

while True:

    success, img = cap.read()
    outputImg = img.copy()
    hands, img = detector.findHands(img)


    if hands:
        hand = hands[0]

        x, y, w, h = hand['bbox']
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgWhite2 = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        imgCrop = img[y - offset:y + h + offset, x - offset: x + w + offset]


        aspectRatio = h / w
        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imCropShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite)
            if time.time() - last_prediction_time >= 2:
                if index == 26:
                    s = s[:-1]
                elif index==27:
                    s = s+" "
                else:
                  s = s+labels[index]
                  print(labels[index])
                last_prediction_time = time.time()



        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imCropShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite)
            if time.time() - last_prediction_time >= 2:
                if index == 26:
                    s = s[:-1]
                elif index == 27:
                    s = s + " "
                else:
                    s = s + labels[index]
                    print(labels[index])
                last_prediction_time = time.time()

        cv2.putText(outputImg, s, (0, 20), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
        cv2.putText(outputImg, labels[index], (x, y), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 2)
    cv2.imshow("Image", outputImg)

    key = cv2.waitKey(1)
    if key == ord("s"):
        print(s)
        url = 'https://www.google.com/search?q={}'.format(s)
        webbrowser.open_new_tab(url)
        break



