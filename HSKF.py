from PIL import Image as PILImage, ImageTk
from tkinter import *
from tkinter import colorchooser
import cv2

def show_frame(frame): 
    frame.tkraise()

 
def colp(section): 
    usecol = colorchooser.askcolor()
    print("Color selected:", usecol)

    hex = usecol[1]

    if hex:
        red = Label(section, text=f"selected {hex}", bg=hex, fg="white").pack()
    
        try:
            with open("color.txt", "a") as file:
                file.write(hex + "\n")
                print("Written to file:", hex)
        except Exception as e:
            print("Failed to write to file:", e)


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

    
