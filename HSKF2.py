from PIL import Image as PILImage, ImageTk
from tkinter import *
from tkinter import colorchooser
import cv2
from HSCR2 import getlimits

def show_frame(frame): 
    frame.tkraise()

 
def colp(section): #function to open the color gui
    usecol = colorchooser.askcolor()
    print("Color selected:", usecol)
    hex = usecol[1]
    if usecol[1]:  
        section.config(fg=usecol[1])
        red = Label(section, text=f"selected {hex}", bg=hex, fg="white").pack()



def opencamera(cap, dihchees, swidth, sheight): #camera feed function 
    
    ret,frame = cap.read()
    if not ret:
        print("failed :(")
        return
    yellow = [255,0,0]
    

    opencv_image = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
    resized = cv2.resize(opencv_image, (swidth, sheight))

    captureim = PILImage.fromarray(resized)
    photoim = ImageTk.PhotoImage(image=captureim)
    dihchees.photoimage = photoim
    dihchees.configure(image=photoim)
    dihchees.after(10,lambda: opencamera(cap, dihchees, swidth, sheight))




    
    