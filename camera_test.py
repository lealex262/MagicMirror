import numpy as np
import cv2

# find camera or webcam
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test-save.avi', fourcc, 20.0, (640,480))

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        out.write(frame)

        # Any color conversions you want here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the frame; if color-converted,
        # replace frame param with the converted frame, e.g. gray
        cv2.imshow('Video Test', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# When everything done, release the capture
cap.release()
out.release()
cv2.destroyAllWindows()