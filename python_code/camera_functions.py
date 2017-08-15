from datetime import datetime
from time import mktime, sleep
import python_code.image_hosting as image_hosting
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
    image_name = generate_image_name()
    camera.capture("./images" + image_name + ".jpg")
    image_hosting.upload_picture(image_name)
    print("Picture taken")

def take_grayscale_image():
    camera.resolution = (2592,1944)
    camera.color_effects = (128, 128)
    image_name = generate_image_name()
    camera.capture("./images" + image_name + ".jpg")
    image_hosting.upload_picture(image_name)
    print("Grayscale picture taken")

def generate_image_name():
    image_name = str(mktime(datetime.now().timetuple()))
    return image_name

take_image() 