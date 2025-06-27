import numpy as np
import cv2 
from PIL import Image as PILImage, ImageTk

def opencamera(cap, dihchees, swidth, sheight):



    captureim = PILImage.fromarray(resized)
    
    photoim = ImageTk.PhotoImage(image=captureim)

    dihchees.photoimage = photoim

    dihchees.configure(image=photoim)

    dihchees.after(10,lambda: opencamera(cap, dihchees, swidth, sheight))
    
    while (1):
        ret,frame = cap.read()
        if not ret:
            print("failed :(")
            return
    
        opencv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)[0][0]
        h,s,v = opencv_image

        resized = cv2.resize(opencv_image, (swidth, sheight))

        upper = np.array([max(h - 10,0),100,100])
        lower = np.array([min(h+10,179),255,255])

        