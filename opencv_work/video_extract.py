import cv2 as cv

video = cv.VideoCapture('/home/mahfuz/Desktop/video/football.mp4')

# Metadata
fps =video.get(cv.CAP_PROP_FPS)
print("Frame per second = ", fps)


# findign the frame at a particular time
minutes = 0
seconds = 30
frame_id = int(fps*(minutes*60 + seconds))
print("Frame_id = ", frame_id)

# extracting the frame form the video
video.set(cv.CAP_PROP_FPS, frame_id)
ret, frame = video.read()

# Displaying and saving the frame
cv.imshow('frame', frame); cv.waitKey(0); cv.destroyAllWindows()
cv.imwrite('my_video_frame.png', frame)