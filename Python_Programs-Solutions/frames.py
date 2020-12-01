# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 20:51:15 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Learn to Code in Tkinter GUI App")

#to display icon of tkinter app
root.iconbitmap('d:/Pictures/python.ico')

frame = LabelFrame(root,text="",padx=50,pady=50)
frame.pack(padx=10,pady=10)

b=Button(frame,text="Don't Click Here !")
b2=Button(frame,text="...or here")
b.grid(row=0,column=0)
b2.grid(row=1,column=1)




root.mainloop()