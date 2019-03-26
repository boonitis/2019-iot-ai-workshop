#!/usr/bin/env python3

import json
import os
import sys
import time
import glob
from datetime import datetime
from itertools import count
import subprocess
import RPi.GPIO as GPIO
from picamera import PiCamera

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)

# Setup PI camera
camera = PiCamera()
camera.resolution = (1600, 1200)


# Initialize the counter
counter = count(start=0,step=1)

option = ""
if len(sys.argv) > 1:
    for arg in sys.argv:
        if arg[0] == "-":
            option = arg[1:]



# Main code goes below here
try:
    while True:

        detect = GPIO.input(4)

        # When PIR sensor detect motion
        if(detect == 1):

            print(next(counter))
            # Start a timer for the whole process

            print("Motion detected")

            # Capture image file using Pi camera (Timestamp as a file name)
            print("Capturing image...")
            file_name = format(datetime.now())
            file_path = os.path.join(os.path.dirname(
                __file__), "captures", file_name+".jpg")
            camera.capture(file_path)
            print("Image captured as: %s" % file_name+".jpg")

            # file_path = 'test-monkey.jpg'
            command = "python3 ./test/recognition.py " + file_name+".jpg"
            os.system(command)
            result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            

            # Delete the image file from this device storage
            if 'k' not in option:
                print("Removing temponary image files...")
                file_list = glob.glob(os.path.join(os.path.dirname(__file__),"captures","*.jpg"))
                for f in file_list:
                    print("%s removed" % f)
                    os.remove(f)

                print("Process successfully complete")


        print(next(counter))
        time.sleep(1)

except KeyboardInterrupt:
    print("\nKeyboardInterrupt: Exit by user")
    camera.close()
    GPIO.cleanup()
except Exception as e:
    print("Errors occured while Kakashi is running: %s" % e)
    camera.close()
    GPIO.cleanup()
