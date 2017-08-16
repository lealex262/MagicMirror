import image_hosting
from cv2 import imwrite
from datetime import datetime
from time import mktime, sleep
from picamera import PiCamera
from picamera.array import PiRGBArray

# find camera or webcam
camera = PiCamera()

def save_video(videoName, timelength):
    # Start Recording
    camera.start_recording(videoName + ".h264")
    sleep(timelength)

    # Stop Recording
    camera.stop_recording()

def take_image():
    camera.resolution = (2592,1944)
    rawCapture = PiRGBArray(camera)
    sleep(0.1)
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    image_path_extension = "../images/" + generate_image_name() + ".jpg"
    imwrite(image_path_extension, image)
    image_hosting.upload_picture(image_path_extension)
    print("Picture taken")

def take_grayscale_image():
    camera.resolution = (2592,1944)
    camera.color_effects = (128, 128)
    rawCapture = PiRGBArray(camera)
    sleep(0.1)
    camera.capture(rawCapture, format="bgr")
    image = rawCapture.array
    image_path_extension = "../images/" + generate_image_name() + ".jpg"
    imwrite(image_path_extension, image)
    image_hosting.upload_picture(image_path_extension)
    print("Grayscale picture taken")

def generate_image_name():
    image_name = str(mktime(datetime.now().timetuple()))
    return image_name

image_hosting.cron_scheduler()
image_hosting.scheduler.start()
while True:
    if raw_input("Press a button to take an image\n"):
        take_image()