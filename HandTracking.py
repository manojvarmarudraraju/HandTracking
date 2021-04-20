import cv2
import mediapipe as mp
import time

# to inititate video capture through webcam
cap = cv2.VideoCapture(0)

# google developed mediapipe for various models in that hands detection is one
# these steps are compulsory to initiate model
mpHands = mp.solutions.hands
hands = mpHands.Hands(False,3)  # Hands will have parameters to handle the situations

# this will be used to draw points on the image
mpDraw = mp.solutions.drawing_utils

cTime = 0
pTime = 0

while True:
    success, img = cap.read()

    # convert image to rgb because mpHands only works for RGB image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # multi_hand_landmarks will detect if hand is present in the image or not
    if results.multi_hand_landmarks:
        # for multiple hands present in the image
        for handlms in results.multi_hand_landmarks:

            for id, lm in enumerate(handlms.landmark):
                h, w, c= img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)

            # draw_landmarks will draw points on our image referencing points found in the draw_landmarks
            # mpHands.HAND_CONNECTIONs will connect points on the image
            mpDraw.draw_landmarks(img, handlms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
