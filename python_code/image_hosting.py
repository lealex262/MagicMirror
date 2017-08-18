from api_credentials import IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, PHONE_NUMBER, FROM_PHONE_NUMBER
from apscheduler.schedulers.background import BackgroundScheduler
from twilio.rest import Client
from imgurpython import ImgurClient
from collections import deque
from datetime import datetime
from os import remove
from time import mktime
from logging import basicConfig

imgur_client = ImgurClient(IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET)
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

basicConfig()
second_interval = 10
hour_interval = 1
scheduler = BackgroundScheduler(job_defaults={'misfire_grace_time': second_interval * 0.5})

delete_hashes = deque([])
seconds_until_deletion = 30

"""
Periodic scheduler to run the check_queue() method
"""
def cron_scheduler():
    scheduler.add_job(check_queue, 'interval', seconds=second_interval)

"""
Upload picture from your computer using the image path
"""
def upload_picture(image_path_extension):
    try:
        # Upload the image to imgur
        picture_info = imgur_client.upload_from_path(image_path_extension)

        # Remove the image from the pi to free up space
        remove(image_path_extension)

        # Delete the image from imgur after a specified amount of time
        deletehash = picture_info[unicode('deletehash', "utf-8")]
        unix_timestamp = picture_info[unicode('datetime', "utf-8")]
        delete_time = int(unix_timestamp) + seconds_until_deletion
        delete_hashes.append((delete_time, deletehash))
        
        print picture_info[unicode('link', "utf-8")]
        
        # Send SMS using imgur link
        twilio_client.messages.create(
            to=PHONE_NUMBER,
            from_=FROM_PHONE_NUMBER,
            body="Picture taken from Magic Mirror",
            media_url=picture_info[unicode('link', "utf-8")])
    except IOError as e:
        print e

"""
Delete an image using an image's delete hash
"""
def delete_image(deletehash):
    imgur_client.delete_image(deletehash)
    print 'Image has been deleted!'

"""
Checks to see if the first element in the queue is past its delete time
"""
def check_queue():
    current_unix_timestamp = mktime(datetime.now().timetuple())
    while len(delete_hashes) != 0 and delete_hashes[0][0] < current_unix_timestamp:
        delete_hash = delete_hashes.popleft()
        delete_image(delete_hash[1])