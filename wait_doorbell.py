import RPi.GPIO as GPIO
import time
import os
from gpiozero import Button

#adjust for where your switch is connected
#buttonPin = 17
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(buttonPin,GPIO.IN)
#print(GPIO.input(buttonPin))

button = Button(17)

while True:
	button.wait_for_press()
	button.wait_for_release()
	#this is the script that will be called (as root)
        #os.system("fswebcam -r 960x720 -d /dev/video0 /home/pi/webcam.jpg")
        os.system("python /home/pi/sendnotify.py")
