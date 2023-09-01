from fastapi import FastAPI, Response
import cv2
import numpy as np

app = FastAPI()

@app.get("/video")
def get_video():
    # Open the video capture
    cap = cv2.VideoCapture("/home/mahfuz/Downloads/momo.mp4")

    # Set the response headers
    headers = {
        "Content-Type": "multipart/x-mixed-replace; boundary=frame",
        "Cache-Control": "no-cache"
    }

    # Create an iterator that returns the frames of the video
    def video_frames():
        while True:
            # Read the next frame from the video capture
            ret, frame = cap.read()

            # If the frame was read successfully, yield it as a JPEG image
            if ret:
                _, jpeg_frame = cv2.imencode(".jpg", frame)
                yield (b"--frame\r\nContent-Type: image/jpeg\r\n\r\n"
                       + jpeg_frame.tobytes() + b"\r\n")
            else:
                # If the frame was not read successfully, break the loop
                break

    # Return the response with the video frames and the appropriate headers
    return Response(video_frames(), headers=headers)
