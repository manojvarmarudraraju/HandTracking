# import time
# import os
import cv2
import HandTrackingModule as htm

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# folderPath = "fingerimages"
# myList = os.listdir(folderPath)
# overlayList = []
# for imPath in myList:
#     image = cv2.imread(folderPath + "/" + imPath)
#     overlayList.append(image)

detector = htm.handDetector(detectionCon=0.75)

tipID = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    num = 0
    if len(lmList) != 0:
        for id in range(0,5):
            if id == 0:
                if lmList[tipID[id]][1] > lmList[tipID[id]-1][1]:
                    num += 1
            else:
                if lmList[tipID[id]][2] < lmList[tipID[id]-2][2]:
                    num += 1
    cv2.putText(img,f'Count: {num}', (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
