from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import colorchooser
import cv2
from HSKF import *
import datetime
import numpy as np
from HSCR import *

root=Tk()
root.title("HueSeeker.V1")
root.minsize(width=700, height=500)

ico = PILImage.open("hueseek.png")
photo= ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


#Intro Startup Page
int1 = Frame(root,bg="#474747") 
int1.pack(fill="both",expand=True)
int1.grid_rowconfigure(0,weight=1)
int1.grid_columnconfigure(0,weight=1)


intro = Frame(int1, bg= "#474747")      
intro.pack(fill="both", expand=True)
desc = Frame(intro,bg= "#474747")
desc.pack(expand=True, pady=(0,150))

logo = PILImage.open("hueseekw.png")
eye = logo.resize((150,150))
eye2= ImageTk.PhotoImage(eye)
eyelog = Label(desc, image=eye2)
eyelog.grid(row=0,column=2)

Label(desc,  text = "HueSeeker",font=("Arial",35),bg= "#474747",fg = "white").grid(row=1,column=2)
Label(desc,  text = "Welcome to Hueseeker V1!",bg= "#474747",font=("Arial",25),fg = "white").grid(row=2,column=2)


act = Button(desc,text = "Activate",command=lambda:(show_frame(mainpag), opencamera(cap, dihchees, swidth, sheight)),height=3,width=15,font=("Arial",15),)
act.grid(row=5,column=2)
#actual program gui screen

mainpag = Frame(int1,bg= "#474747")
Label(mainpag,text="HueseekerV1",bg= "#474747",fg = "white")
mainpag.pack()
#camera feed display
dihscreen = Frame(mainpag, bg="#000000",)
dihscreen.pack(side="left",anchor="w",padx=10,pady=10)
dihchees = Label(dihscreen,bg="black")
dihchees.pack()

swidth=550
sheight=400


cap = cv2.VideoCapture(0)
width = 550
height = 400
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


''' left side of HueSeeker, logs, color selection'''
gooningL = Frame(mainpag,bg= "#474747")
    
gooningL.pack(side="right",anchor="se",fill=BOTH,expand=True)

Button(gooningL,text="Quit Hueseeker",command=root.destroy,fg="red",bg="grey").pack(anchor="ne", padx= 15,expand=True)

Label(gooningL,text="Records",fg="white",bg="#242526").pack()
logscreen = Frame(gooningL, bg="#242526", height=200, width=200)

logscreen.pack(side="top", anchor="ne",padx=5,pady=1,fill=BOTH,expand=True)


Label(gooningL, fg="white",text="Insert Color Here",bg="#474747").pack(anchor='e',expand=True,fill=BOTH,padx=5)
usebut=Button(gooningL,text="Input Desired Color", command=lambda:(colp(section),)).pack(anchor='e',expand=True,fill=BOTH,padx=5,pady=1)

section = Frame(gooningL, bg="#242526",height=100,width=200)

section.pack(side="bottom", anchor="ne",padx=5,pady=1,fill=BOTH,expand=True)


    
show_frame(intro)


root.mainloop()