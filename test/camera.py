#!/usr/bin/env python3

import json
import os
import sys
import time
import glob
from datetime import datetime
from itertools import count

import RPi.GPIO as GPIO
from picamera import PiCamera

# Setup GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, GPIO.PUD_DOWN)

# Setup PI camera
camera = PiCamera()
camera.resolution = (1600, 1200)
camera.start_preview()
sleep(10)
camera.stop_preview()