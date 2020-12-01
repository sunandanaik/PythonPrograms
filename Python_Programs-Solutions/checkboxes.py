# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 00:19:42 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Learn to Code in GUI App')
root.geometry("400x400") #set size of root window


def show():
    mylabel=Label(root,text=var.get()).pack()


#declaring a integer variable
#var = IntVar()
#to declare string variable
var = StringVar()

#to build checkbox
c=Checkbutton(root,text="Check this box!!",variable=var,onvalue="On",offvalue="Off")
c.deselect()
c.pack()

#mylabel=Label(root,text=var.get()).pack()
mybtn=Button(root,text="Show Selection",command=show).pack()

root.mainloop()