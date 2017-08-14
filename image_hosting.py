from imgurpython import ImgurClient
from api_credentials import IMGUR_CLIENT_ID, IMGUR_CLIENT_SECRET
from apscheduler.schedulers.blocking import BlockingScheduler
from collections import deque
from datetime import datetime
from time import mktime

client_id = IMGUR_CLIENT_ID
client_secret = IMGUR_CLIENT_SECRET
client = ImgurClient(client_id, client_secret)

scheduler = BlockingScheduler()
second_interval = 10
hour_interval = 1

delete_hashes = deque([])
seconds_until_deletion = 30

def cron_scheduler():
    scheduler.add_job(check_queue, 'interval', seconds=second_interval)

"""
Upload picture from your computer using the image path
"""
def upload_picture():
    picture_info = client.upload_from_path("./test.jpg")
    deletehash = picture_info[unicode('deletehash', "utf-8")]
    unix_timestamp = picture_info[unicode('datetime', "utf-8")]
    delete_time = int(unix_timestamp) + seconds_until_deletion
    delete_hashes.append((delete_time, deletehash))
    print picture_info[unicode('link', "utf-8")]

"""
Delete an image using an image's delete hash
"""
def delete_image(deletehash):
    client.delete_image(deletehash)

"""
Checks to see if the first element in the queue is past its delete time
"""
def check_queue():
    current_unix_timestamp = mktime(datetime.now().timetuple())
    while len(delete_hashes) != 0 and delete_hashes[0][0] < current_unix_timestamp:
        delete_hash = delete_hashes.popleft()
        delete_image(delete_hash[1])

upload_picture()
cron_scheduler()
scheduler.start()
