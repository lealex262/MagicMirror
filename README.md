# Magic Mirror

Current Capabilities:
* Concurrent GUI and video stream
* Fist gesture recognition to initiate picture countdown on GUI
* Taking a picture -> hosting it on Imgur -> deleting from local storage -> deleting from Imgur after given time period
* Send media or image link to phone number via SMS

Tasks:
* Optimize gesture recognition
* Improve and add more info/visuals on GUI
* Improve the mirror display/frame

Possible Tasks:
* Recognition of more/different gestures
* SMS for multiple phone numbers instead of a single one

Commands:
* Install required dependencies by installing pip then doing *pip install -r requirements.txt --user*
* To update package list, pip install your package then *pip freeze > requirements.txt* or manually adding to the requirements.txt file (recommended)
* To rotate the raspberry pi screen, do 1) *sudo nano /boot/config.txt* OR *sudo vim /boot/config.txt* OR just open up that file, 2) add *display_rotate=1* to the last line of that file, and 3) *sudo reboot* 
* To display raspberry pi temperature, run *watch /opt/vc/bin/vcgencmd measure_temp*
