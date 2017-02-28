#! /usr/bin/env python3
# coding = utf-8

# spiralDraw.py - draw picture.

import pyautogui
import time

time.sleep(5)
pyautogui.click()

distance = 200
while distance > 0:
    # move right
    pyautogui.dragRel(distance, 0, duration=0.2)
    # move down
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration=0.2)
    # move left
    pyautogui.dragRel(-distance, 0, duration=0.2)
    # move up
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration=0.2)


