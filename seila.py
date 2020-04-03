import numpy as np
import argparse
import imutils
import cv2
import pyautogui
import time


aux = 0

pyautogui.moveTo(round(pyautogui.size()[0]/2),round(pyautogui.size()[1]/2)+53)
pyautogui.drag(0,pyautogui.size()[1],1, button='right')
pyautogui.moveTo(round(pyautogui.size()[0]/2),round(pyautogui.size()[1]/2)+54)
pyautogui.drag(0,pyautogui.size()[1],1, button='right')