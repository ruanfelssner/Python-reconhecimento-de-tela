import numpy as np
import argparse
import imutils
import cv2
import pyautogui
import time

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
pyautogui.click(10 , 10)
loopCount = 0
for c in cnts:
    aux = 0
    if (len(c)<=50):
        loopCount = len(c)
    else:
        loopCount = round(len(c) * 0.05)
    aux = loopCount
    print (len(c))
    for points in c:
        if(loopCount == aux and points[0][1] > 100):
            print("mexe")
            print(round(points[0][0]/2))
            print(round(points[0][1]/2))
            pyautogui.click(round(points[0][0]/2) , round(points[0][1]/2))
            aux = 0
        elif ((c[len(c) -1][0][0] == points[0][0]) and (c[len(c) -1][0][1] == points[0][1]) and points[0][1] > 100):
            print("fim")
            print(round(c[0][0][0]/2))
            print(round(c[0][0][1]/2))
            time.sleep(1)
            pyautogui.click(round(c[0][0][0]/2) , round(c[0][0][1]/2))
            time.sleep(3)
            
        aux +=1
print("comeca de novo")
cv2.waitKey(0)
