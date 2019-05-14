import numpy as np
import cv2 as cv

# Setup array to keep track of recent frames
history = []

# Capture default camera
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    height, width, channels = frame.shape

    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    history.append(frame)
    if len(history) > 60:
        history.remove(history[0])

    output = history[0]

    for i in range(len(history)):
        output = cv.addWeighted(output, 0.9, history[i], 0.1, 0)

    # Display the resulting frame
    cv.imshow('frame', output)
    wait = cv.waitKey(1)
    if wait == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
