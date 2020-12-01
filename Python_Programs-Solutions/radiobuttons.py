# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:00:09 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Learn to Code in Tkinter GUI App")

#to display icon of tkinter app
root.iconbitmap('d:/Pictures/python.ico')

r= IntVar()
#r.set("2")




def clicked(value):
    mylabel=Label(root,text=r.get())
    mylabel.pack()

Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:clicked(r.get())).pack()
Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda:clicked(r.get())).pack()

mylabel=Label(root,text=r.get())
mylabel.pack()
myButton=Button(root,text="Click Me!",command=lambda:clicked(r.get()))
myButton.pack()

root.mainloop()