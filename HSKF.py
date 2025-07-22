from tkinter import *
import cv2  
import numpy as np
from tkinter import colorchooser
import cv2

def show_frame(frame): 
    frame.tkraise()

 
def colp(section): 
    usecol = colorchooser.askcolor()  #store to to txt file function
    print("Color selected:", usecol)


    hex = usecol[1]

    if usecol[0] is None:
        return None,None

    if hex:
        red = Label(section, text=f"selected {hex}", bg=hex, fg="white").pack()
    
        try:
            with open("color.txt", "a") as file:
                file.write(hex + "\n")
                print("Written to file:", hex)
        except Exception as e:
            print("Failed to write to file:", e)
    