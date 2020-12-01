# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 23:26:35 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title('Learn to Code in GUI App')

#showinfo,showwarning,showerror,askquestion,askokcancel,askyesno-diff types of messageboxes

def popup():
    #messagebox.showinfo("This is my popup!","Hello World!")
    #messagebox.showerror("This is my popup!","Hello World!")
    response=messagebox.askquestion("This is my popup!","Hello World!")
    Label(root,text=response).pack()
    if response =="yes":
        Label(root,text="You clicked Yes!!").pack()
    else:
       Label(root,text="You clicked No!!").pack() 



#to create message box
Button(root,text="Popup",command=popup).pack()










root.mainloop()