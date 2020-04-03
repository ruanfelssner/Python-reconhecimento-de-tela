import numpy as np
import argparse
import imutils
import cv2
import pyautogui
import time
import sys

count = 0

while count <= 7:        
    pyautogui.MINIMUM_DURATION = 0.001
    pyautogui.screenshot("imagem.png")
    pyautogui.FAILSAFE = False
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help = "imagem.png")
    args = vars(ap.parse_args())

    # load the image
    image = cv2.imread(args["image"])

    lower = np.array([0, 0, 0])
    upper = np.array([15, 15, 15])
    shapeMask = cv2.inRange(image, lower, upper)

    # find the contours in the mask
    cnts = cv2.findContours(shapeMask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    print("I found {} black shapes".format(len(cnts)))

    #for c in cnts:
        # draw the contour and show it
        #cv2.drawContours(image, [c], -1, (0, 255, 0), 2)
        #cv2.imshow("Image", image)
        #cv2.waitKey(0)
    # loop over the contours
    pyautogui.click(500 , 500)
    loopCount = 0
    aux = 0
    for c in cnts:
        if (len(c)<=50):
            loopCount = len(c)
        else:
            loopCount = round(len(c) * 0.01)
        aux = loopCount
        print (loopCount,aux)
        for points in c:
            if(aux >= loopCount and points[0][0] < 2700):
                print(points[0])
                pyautogui.click(round(points[0][0]/2) , round(points[0][1]/2))
                aux = 0    
            aux +=1
        time.sleep(1)
        pyautogui.rightClick(600,600)
    
    print(pyautogui.size()[0])
    pyautogui.moveTo(round(pyautogui.size()[0]/2),0)
    pyautogui.drag(0,pyautogui.size()[1],1, button='right')
    pyautogui.moveTo(round(pyautogui.size()[0]/2),round(pyautogui.size()[1]/2))
