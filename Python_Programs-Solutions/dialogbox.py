# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:53:55 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

root=Tk()
root.title('Learn to Code in GUI App')

#1
#root.filename=filedialog.askopenfilename(initialdir="/d:/Pictures",title="Select a file",filetypes=(("png files","*.png"),("All files","*.*")))

#my_label=Label(root,text=root.filename).pack()
#my_image=ImageTk.PhotoImage(Image.open(root.filename))
#my_img_label=Label(image=my_image).pack()

#2
def open():
    #pass
    global my_image
    root.filename=filedialog.askopenfilename(initialdir="/d:/Pictures",title="Select a file",filetypes=(("png files","*.png"),("All files","*.*")))

    my_label=Label(root,text=root.filename).pack()
    my_image=ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label=Label(image=my_image).pack()

mybtn=Button(root,text="Open File",command=open).pack()

root.mainloop()