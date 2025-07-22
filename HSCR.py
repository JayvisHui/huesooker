import numpy as np
import cv2 
from PIL import Image as PILImage, ImageTk

def opencamera(cap, dihchees, swidth, sheight):

    ret,frame = cap.read()
    if not ret:
        print("failed :(")
        return
    



    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)    
   
    resized = cv2.resize(hsv, (swidth, sheight))

    captureim = PILImage.fromarray(resized)
    
    photoim = ImageTk.PhotoImage(image=captureim)

    dihchees.configure(image=photoim)
    dihchees.photoimage = photoim

    dihchees.after(10,lambda: opencamera(cap, dihchees, swidth, sheight))

    kernal = np.ones((5,5),"uint8")

    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.dilate(mask,np.ones((5,5), "uint8"))
    res = cv2.bitwise_and(frame, frame, mask=mask)


    contours,ret = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if (area > 300):
            x,y,w,h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255),2)
            thetext = cv2.putText(imageFrame, "Custom Color #1", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1.0,(0,0,255))

    
    

        