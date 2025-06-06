from PIL import Image as PILImage, ImageTk
from tkinter import *
from tkinter import colorchooser
import cv2
from tkinter import Label 



def show_frame(frame):
    frame.tkraise()

def shutthefuckup(root):
    root.destroy()


def colp(gooningL):
    usecol = colorchooser.askcolor()
    recol = Label(gooningL, text=usecol).pack()