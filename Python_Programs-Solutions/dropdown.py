# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 00:28:37 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Learn to Code in GUI App')
root.geometry("400x400") #set size of root window

def show():
    mylabel=Label(root,text=clicked.get()).pack()
    

#declare string variable
clicked=StringVar()

options=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
clicked.set(options[0])

#Drop down boxes
drop=OptionMenu(root,clicked,*options)
drop.pack()

mybtn=Button(root,text="Show Selection",command=show).pack()

root.mainloop()