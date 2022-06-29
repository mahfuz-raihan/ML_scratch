# here we try to capture the frame from a video file.

import numpy as np
import cv2 as cv

# open the inbuilt camera of laptop to capture video
cap = cv.VideoCapture('football.mp4')
i = 0
while (cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == False:
        break
    
    # save the image frame by frame
    cv.imwrite('frame'+str(i)+'.jpg', frame)
    i += 1
    
cap.release()
cv.destroyAllWindows()