from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk, ImageFilter
import cv2
import numpy as np
from datetime import datetime
import _thread
import time

def openSetDetect(master,filepathval):
    ws = tk.Toplevel(master)
    ws.geometry('1100x480')
    ws.title('HTML Code Generator')
    ws.config(bg='#FFCC66')

    al1 = Label(ws,text="Image",height=1,width=20,fg="black",bg="#FFCC66",font=("arial italic", 15))
    Signalpics1=Label(ws,fg="black",bg='#0000ff')
    Signalpics1.place(x=10, y=60)

    img = Image.open(filepathval)
    img = img.resize((480, 380), Image.Resampling.LANCZOS);
    imgtk = ImageTk.PhotoImage(image=img)
    Signalpics1.imgtk = imgtk
    Signalpics1.configure(image=imgtk)
            
    al2 = Label(ws,text="OUTPUT",height=1,width=20,fg="black",bg="#FFCC66",font=("arial italic", 15))

    #aa1 = tk.StringVar()
    #a1 = tk.Entry(ws,width=33,textvariable=aa1,font=("arial italic", 8), fg="Black")

    text1=tk.Text(ws,font=("arial italic", 10),bg="white", fg="black",height=20,width=70)


    al1.place(x=10, y=10)

    al2.place(x=500, y=10)
    #a1.place(x=580, y=90)
    text1.place(x=500, y=60)

    
    ws.mainloop()
