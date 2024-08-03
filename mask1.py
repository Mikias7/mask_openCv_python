#mask 
import cv2 as cv
import numpy as np


cap = cv.VideoCapture(1)

while True:
    ret, frame = cap.read()

    (h1,w1) = frame.shape[:2]
    (h2,w2) = frame.shape[:2]

    blank = np.zeros(frame.shape[:2],dtype='uint8')
    #draw rectangle for mask 
    

    mask = cv.rectangle(blank, (w2//2 + 50,h2//2 - 35), (w1-150,h1-95), 255,-1)
    masked = cv.bitwise_and(frame,frame, mask=mask)
    cv.imshow("frame", masked)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()