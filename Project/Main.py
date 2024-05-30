from tkinter.ttk import *
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import output

master = tk.Tk()
master.title("HTML Code Generator")
master.geometry("900x400")
#master.resizable(False, False)
master.configure(background='#FFCC66')

def file_opener1():
    input11 =filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("[png]","*.png*"),("[PNG]","*.PNG*"),("[jpg]","*.jpg*"),("[JPG]","*.JPG*"),("all files","*.*")))
    filepath.set(input11)

def Train_file():
    pass

def Process_file():
    if filepath.get()!='':
        output.openSetDetect(master,filepath.get())
    else:
        messagebox.showinfo(title="Alert Message", message="Select File")
        


label = tk.Label(master ,width=40,text = "HTML Code Generator",font=("arial italic", 30), bg="#FF9900", fg="white").grid(row=0, column=0,columnspan=2)


btnfile = tk.Button(master,text="Select HTML Page Image File",font=("arial italic", 15), bg="#0000FF", fg="white",width=25,command=file_opener1).grid(row=1, column=0,padx=5, pady=20)
a = tk.Label(master ,width=25,text = "Selected Image",font=("arial italic", 15), bg="#FFCC66", fg="#0000FF").grid(row=2, column=0,padx=5, pady=5)
filepath = tk.StringVar()
a1 = tk.Entry(master,font=("arial italic", 15), bg="white", fg="Blue",width=25,textvariable=filepath).grid(row=3, column=0,padx=5, pady=5)
filepath.set("");

btn1 = tk.Button(master,text="Train Model",font=("arial italic", 15), bg="#0000FF", fg="white",width=25,command=lambda:Train_file()).grid(row=1, column=1,padx=5, pady=20)

btn2 = tk.Button(master,text="Generator Code",font=("arial italic", 15), bg="#0000FF", fg="white",width=25,command=lambda:Process_file()).grid(row=2, column=1,padx=5, pady=20)

btn3 = tk.Button(master,text="Exit",font=("arial italic", 15), bg="#0000FF", fg="white",width=25,command=master.destroy).grid(row=3, column=1,padx=5, pady=20)


master.mainloop()
