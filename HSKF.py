from tkinter import *
import cv2.cv2
import numpy as np
from tkinter import colorchooser
import cv2
from PIL import Image as PILImage, ImageTk
 
def show_frame(frame):
    frame.tkraise()


def colp(section): 

    usecol = colorchooser.askcolor()  #store to to txt file function
    print("Color selected:", usecol)
    hex = usecol[1]

    
    
def opencamera(cap, dihchees, swidth, sheight):

    ret,frame = cap.read()
    if not ret:
        print("failed :(")
        return

    cv2.imwrite("debug_raw.jpg", frame)

    resized = cv2.resize((swidth, sheight))

    captureim = PILImage.fromarray(resized)
    
    photoim = ImageTk.PhotoImage(image=captureim)

    dihchees.configure(image=photoim)
    dihchees.photoimage = photoim

    dihchees.after(10,lambda: opencamera(cap, dihchees, swidth, sheight))

