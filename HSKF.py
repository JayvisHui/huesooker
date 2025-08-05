from PIL import Image as PILImage, ImageTk
from tkinter import *
from tkinter import colorchooser
import cv2
from HSCR import getlimits

def show_frame(frame): 
    frame.tkraise()

 
def colp(section): #function to open the color gui
    usecol = colorchooser.askcolor()
    print("Color selected:", usecol)
    hex = usecol[1]
    if usecol[1]:  
        section.config(fg=usecol[1])
        red = Label(section, text=f"selected {hex}", bg=hex, fg="white").pack()





def opencamera(cap, dihchees, swidth, sheight):
    
    ret,frame = cap.read()
    if not ret:
        print("failed :(")
        return
    yellow = [255,0,0]
    
    llimit, ulimit = getlimits(yellow)

    opencv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
    resized = cv2.resize(opencv_image, (swidth, sheight))

    captureim = PILImage.fromarray(resized)
    photoim = ImageTk.PhotoImage(image=captureim)
    dihchees.photoimage = photoim
    dihchees.configure(image=photoim)
    dihchees.after(10,lambda: opencamera(cap, dihchees, swidth, sheight))

    s = cv2.inRange(llimit, ulimit)
    mask = PILImage.fromarray(s)

    bbox = mask.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox 
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0),5)



    
    