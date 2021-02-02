"""
캠 ON 기능
"""

import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set Width
cap.set(4, 480)  # set Height
while (True):

    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip camera vertically //상하 반전 0,1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
