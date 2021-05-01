import cv2
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)
wCam, hCam = 1000, 1000
cap.set(3, wCam)
cap.set(4, hCam)

handTracker = htm.handDetector(maxHands=2)

arr = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()

    handTracker.findHands(img)
    positions1 = handTracker.findPosition(img, draw=False)
    try:
        positions2 = handTracker.findPosition(img, handNo=1, draw=False)
        if len(positions1) != 0 and len(positions2) != 0:
            for i in arr:
                cv2.line(img, (positions1[i][1], positions1[i][2]), (positions2[i][1], positions2[i][2]), (255, 0, 255),
                         3)
    except:
        print("Only one hand is in the image")

    cv2.imshow("Image", img)

    cv2.waitKey(1)
