"""call this module to setup your python packages via pip"""

from pip._internal import main as pip

pip_install_argument = "install"

# packages to install
packages_to_install = [
        "tensorflow"
        "numpy",        # math magic 1
        "scipy",        # math magic 2
        "tensorflow_hub",
        ]

def install(packages):
    """installes given packages via pip

    Args:
        package names as list

    Returns:
        None

    """
    global pip_install_argument
    for package in packages:
        pip([pip_install_argument, package])

if __name__ == '__main__':
    install(packages_to_install)

#!/usr/bin/env python3

import json
import os
import sys
import time
import glob
from datetime import datetime
from itertools import count

import RPi.GPIO as GPIO
from modules import photograph
from modules.clock import Clock
from picamera import PiCamera

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)

# Setup PI camera
camera = PiCamera()
camera.resolution = (1600, 1200)

# Setup Performance Timers
timer_all = Clock()

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

            # file_path = 'test-monkey.jpg'

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
