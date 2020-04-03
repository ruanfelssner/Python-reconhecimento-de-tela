import time
import os
import sys
from functools import partial
import pyautogui
import cv2
import numpy as np 


count = 0

while count <= 0:
    print(pyautogui.size()[0])
    pyautogui.moveTo(round(pyautogui.size()[0]/2),0)
    pyautogui.drag(0,pyautogui.size()[1],1, button='right')
    pyautogui.moveTo(round(pyautogui.size()[0]/2),round(pyautogui.size()[1]/2))

    pyautogui.screenshot("imagem.png")
    img = cv2.imread('imagem.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,5,3,0.04)
    ret, dst = cv2.threshold(dst,0.1*dst.max(),255,0)
    dst = np.uint8(dst)
    ret, labels, stats, centroids = cv2.connectedComponentsWithStats(dst)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.001)
    corners = cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)
    print (len(corners))
    for i in range(1, len(corners)):
        pyautogui.click(round(corners[i][0]/2),round(corners[i][1]/2))
    count += 1

