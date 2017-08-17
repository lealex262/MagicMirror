import image_hosting
from cv2 import imwrite
from datetime import datetime
from time import mktime, sleep
from picamera import PiCamera
from picamera.array import PiRGBArray

def save_video(videoName, timelength):
    # Start Recording
    camera.start_recording(videoName + ".h264")
    sleep(timelength)

    # Stop Recording
    camera.stop_recording()

def take_image(grayscale=False):
    camera = PiCamera()
    camera.resolution = (2592,1944)
    if grayscale:
        camera.color_effects(128, 128)
    rawCapture = PiRGBArray(camera, size=(2592,1944))
    sleep(0.1)
    camera.capture(rawCapture, format="bgr", use_video_port=False)
    image = rawCapture.array
    image_path_extension = "../images/" + generate_image_name() + ".jpg"
    imwrite(image_path_extension, image)
    image_hosting.upload_picture(image_path_extension)
    print("Picture taken")
    camera.close()
    sleep(2)

def generate_image_name():
    image_name = str(mktime(datetime.now().timetuple()))
    return image_name

def scheduler_setup():
    image_hosting.cron_scheduler()
    image_hosting.scheduler.start()