import numpy as np
import cv2
from time import time

def detect_fist():
    timer_started = False
    start_time = 0
    end_time = 0
    count = 0
    cap = cv2.VideoCapture(0)

    # classifier for closed right fist
    fist_cascade = cv2.CascadeClassifier('../classifier/haarcascade_fist.xml')
    while (1):
        if timer_started:
            end_time = time()
            # if it's been less than 5 seconds and we get 50 counts of fist recognition, break
            if end_time - start_time < 5 and count > 50:
                break
            # otherwise if it's been more than 5 seconds, reset the timer and count
            elif end_time - start_time > 5:
                timer_started = False
                count = 0

        ret, frame = cap.read()

        # draw rectangles around fist
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        fists = fist_cascade.detectMultiScale(gray, 1.3, 5)
        if len(fists) != 0:
            if not timer_started:
                timer_started = True
                start_time = time()
                print start_time
            count += 1
            print count
        for (x, y, w, h) in fists:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            frame[y: y + h, x: x + w] = hsv[y: y + h, x: x + w]

        cv2.imshow('img', frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

def take_image(imageName):
    ret, frame = cap.read()
    cv2.imwrite(imageName, frame)

detect_fist()