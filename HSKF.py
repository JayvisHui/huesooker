from PIL import Image as PILImage, ImageTk
from tkinter import *
from tkinter import colorchooser
import cv2




def show_frame(frame): 
    frame.tkraise()

def shutthefuckup(root): #function to close Hueseeker
    root.destroy() 

 
def colp(gooningL): #function to open the color gui
    usecol = colorchooser.askcolor()
    recol = Label(gooningL, text=usecol).pack()