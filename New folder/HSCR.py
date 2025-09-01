import numpy as np
import cv2


def getlimits(color):
    c = np.uint([[color]])
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    hue = hsvC [0][0][0]

    if hue >= 165:
        llimit = np.array([hue - 10,100,100], dtype = np.uint8)
        ulimit = np.array([180,255,255],dtype=np.uint8)
    elif hue <= 15:  # Lower limit for divided red hue
        llimit = np.array([0, 100, 100], dtype=np.uint8)
        ulimit = np.array([hue + 10, 255, 255], dtype=np.uint8)
    else:
        llimit = np.array([hue - 10, 100, 100], dtype=np.uint8)
        ulimit = np.array([hue + 10, 255, 255], dtype=np.uint8)

    return llimit, ulimit


        