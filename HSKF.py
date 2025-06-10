from PIL import Image as PILImage, ImageTk
from tkinter import *
from tkinter import colorchooser
import cv2

def show_frame(frame): 
    frame.tkraise()

 
def colp(gooningL): #function to open the color gui
    usecol = colorchooser.askcolor()
    recol = Label(gooningL, text=usecol).pack()


def opencamera(cap, dihchees, swidth, sheight):

    ret,frame = cap.read()
    if not ret:
        print("failed :(")
        return
    
    opencv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)

    resized = cv2.resize(opencv_image, (swidth, sheight))

    captureim = PILImage.fromarray(resized)
    
    photoim = ImageTk.PhotoImage(image=captureim)

    dihchees.photoimage = photoim

    dihchees.configure(image=photoim)

    dihchees.after(10,lambda: opencamera(cap, dihchees, swidth, sheight))

    
