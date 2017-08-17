import camera_functions
import numpy as np
import cv2
from time import time, sleep
from picamera.array import PiRGBArray
from picamera import PiCamera

def detect_fist(event, queue):
    camera = PiCamera()
    camera.resolution = (1296,972)
    camera.framerate = 25
    rawCapture = PiRGBArray(camera, size=(1296,972))
    timer_started = False
    start_time = 0
    end_time = 0
    count = 0
    
    sleep(0.1)
    
    fist_cascade = cv2.CascadeClassifier('../classifier/haarcascade_fist.xml')
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        if timer_started:
            end_time = time()
            # if it's been less than 7 seconds and we get 2 counts of fist recognition, break
            if end_time - start_time < 7 and count > 0:
                queue.put("Test")
                event.set
                return
            # otherwise if it's been more than 7 seconds, reset the timer and count
            elif end_time - start_time > 7:
                timer_started = False
                count = 0
        image = frame.array
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        fists = fist_cascade.detectMultiScale(gray, 1.3, 5)
        if len(fists) != 0:
            print fists
            if not timer_started:
                timer_started = True
                start_time = time()
            count += 1
        cv2.imshow("Detection", image)
        key = cv2.waitKey(1) & 0xFF
            
        """
        for (x, y, w, h) in fists:
            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            image[y: y + h, x: x + w] = hsv[y: y + h, x: x + w]
        
        cv2.imshow("Detection", image)
        key = cv2.waitKey(1) & 0xFF
        """
        
        rawCapture.truncate(0)
        
def initiate_countdown(camera):
    initial_count = 3
    while initial_count > 0:
        sleep(1)
        print initial_count
        initial_count -= 1    
    print "Say Cheese!"
    camera_functions.take_image(camera)
    detect_fist()