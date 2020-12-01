# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 00:07:21 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('Learn to Code in GUI App')
root.geometry("400x400") #set size of root window

#to fetch value of horizontal slider and display in label
def slide():
    my_label=Label(root,text=horizontal.get()).pack()
    root.geometry(str(horizontal.get())+"x"+ str(vertical.get()))

vertical=Scale(root,from_=0,to=400)
vertical.pack()

horizontal=Scale(root,from_=0,to=400,orient=HORIZONTAL)
horizontal.pack()

my_label=Label(root,text=horizontal.get()).pack()

mybtn=Button(root,text="Click ME",command=slide).pack()

root.mainloop()