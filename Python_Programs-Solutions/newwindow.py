# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:40:37 2020

@author: DELL
"""

#Creating new window 
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Learn to Code in GUI App')


def open():
    global my_img
    top=Toplevel()
    top.title("My Second Window")
    top.iconbitmap('d:/Pictures/python.ico')
    lbl=Label(top,text="Hello World").pack()
    my_img=ImageTk.PhotoImage(Image.open("d:/Pictures/running2.jpg"))
    my_label=Label(top,image=my_img).pack()
    btn2=Button(top,text="Close WIndow",command=top.destroy).pack()

btn=Button(root,text="Open Second Window", command=open).pack()

#top=Toplevel()
#top.title("My Second Window")
#top.iconbitmap('d:/Pictures/python.ico')
#lbl=Label(top,text="Hello World").pack()
#my_img=ImageTk.PhotoImage(Image.open("d:/Pictures/running2.jpg"))
#my_label=Label(top,image=my_img).pack()













root.mainloop()