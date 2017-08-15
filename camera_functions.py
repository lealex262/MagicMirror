from datetime import datetime
from time import mktime, sleep
import numpy as np
# import cv2
import picamera

# find camera or webcam
camera = picamera.PiCamera()

def save_video(videoName, timelength):
    # Start Recording
    camera.start_recording(videoName + ".h264")
    sleep(timelength)

    # Stop Recording
    camera.stop_recording()

def take_image():
    camera.resolution = (2592,1944)
    camera.capture(generate_image_name() + ".jpg")
    print("Picture taken")

def take_grayscale_image():
    camera.resolution = (2592,1944)
    camera.color_effects = (128, 128)
    camera.capture(generate_image_name() + ".jpg")
    print("Grayscale picture taken")

def generate_image_name():
    image_name = str(mktime(datetime.now().timetuple()))
    return image_name

# save_video("test", 5) 
take_image() 