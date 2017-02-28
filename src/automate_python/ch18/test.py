#! /usr/bin/env python3
# coding = utf-8

# test.py - some statement run test.

import pyautogui

# 获取屏幕分辨率
print(pyautogui.size())
# 移动鼠标
for i in range(10):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
