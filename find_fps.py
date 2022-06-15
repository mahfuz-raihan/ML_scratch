import numpy as np
import cv2 as cv
import time # time count

# capture a vido clip object and read from input file
capture = cv.VideoCapture('vdo.mp4') # r = for read the file
# use the video record time for last frame
past_frame_time = 0

# use the current frame from the video
current_frame_time = 0

# check if camera opend successfully
if (capture.isOpened() == False):
    print('Error opening video file')

while capture.isOpened():
    
    # capture the video frame by frame
    ret, frame = capture.read()
    
    # if video finished or no video input found
    if not ret:
        break
    
    # out operations on the frame come here
    gray = frame
    
    # resize the frame size according to our need
    gray = cv.resize(gray, (500, 300)) # (1620, 720) = define the dimention or resulation
    
    # font which we will be using to display FPS
    font = cv.FONT_HERSHEY_SCRIPT_COMPLEX  # opencv dwaring function-font to diplay the context
    
    # time when we finish processing for this frame
    current_frame_time = time.time()
    
    # calculate the FPS
    fps = 1/(current_frame_time - past_frame_time)
    
    # assign the current frame time to past frame time
    past_frame_time = current_frame_time
    
    # convert the fps into integer
    fps = int(fps)
    
    '''
    convert the fps to string so that we can display it on
    frame by suing putText function
    '''
    fps = str(fps)
    
    # putting the fps count on the frame
    cv.putText(gray, fps, (3, 100), font, 1, (0, 254, 0), 2, cv.LINE_AA) 
    
    # displying the frame with fps
    cv.imshow('Picture', gray)
    
    # press 'Q' if you want to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# when everything done, release the caputre
capture.release()

# destroy all the windows now
cv.destroyAllWindows()