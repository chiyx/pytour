#! /usr/bin/env python3
# coding = utf-8

import time
import subprocess
import sys
import os

timeLeft = 60
while timeLeft > 0:
    print(timeLeft, end=' ')
    time.sleep(1)
    timeLeft = timeLeft - 1

baseDir = os.path.split(os.path.realpath(__file__))[0]
resourcesDir = os.path.split(baseDir)[0]
subprocess.Popen(['open', resourcesDir + '/resources/alarm.wav'])
