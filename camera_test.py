import numpy as np
import cv2
import picamera

def camera_functions():

    # find camera or webcam
    camera = picamera.PiCamera()

    def save_video(videoName, timelength):
        # Start Recording
        camera.start_recording(videoName + ".h264")
        sleep(timelength)

        # Stop Recpording
        camera.stop_recording()

    def take_image(imageName):
        camera.resolution = (2592,1944)
        camera.capture(imageName + ".jpg")
        print("Picture " + imageName + " taken")
        
    def take_grayscale_image(imageName):
        camera.resolution = (2592,1944)
        camera.color_effects = (128, 128)
        camera.capture(imageName + ".jpg")
        print("Picture " + imageName + " taken")
 
camera_functions()