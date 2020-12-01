# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 21:14:48 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Learn to Code in Tkinter GUI App")

#to display icon of tkinter app
root.iconbitmap('d:/Pictures/python.ico')

Toppings=[("Pepperoni","Pepperoni"),
       ("Cheese","Cheese"),
       ("Mushroom","Mushroom"),
       ("Onion","Onion")]

pizza = StringVar()
pizza.set("Pepperoni")


for text,mode in Toppings:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)
    
def clicked(value):
    mylabel=Label(root,text=pizza.get())
    mylabel.pack()    
    
myButton=Button(root,text="Click Me!",command=lambda:clicked(pizza.get()))   
myButton.pack()  
mylabel=Label(root,text=pizza.get())
mylabel.pack()
  
root.mainloop()