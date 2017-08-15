from datetime import datetime
from time import mktime, sleep
import image_hosting
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
    image_path_extension = "../images/" + generate_image_name() + ".jpg"
    camera.capture(image_path_extension)
    image_hosting.upload_picture(image_path_extension)
    print("Picture taken")

def take_grayscale_image():
    camera.resolution = (2592,1944)
    camera.color_effects = (128, 128)
    image_path_extension = "../images/" + generate_image_name() + ".jpg"
    camera.capture(image_path_extension)
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