# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 08:41:41 2020

@author: DELL
"""
from tkinter import *
root= Tk()


#Creating input box
e=Entry(root,width=50,bg="grey",fg="blue",borderwidth=5)
e.insert(0,"Enter Name")

#function defined
def myClick():
    hellovar="Hello "+e.get()
    myLabel=Label(root,text=hellovar)
    myLabel.pack()

#Creating a label widget
myLabel1=Label(root,text="Hello Tkinter!!!")
myLabel2=Label(root,text="My Name is Sunanda!!!")

#Placing the labels in grids
#myLabel1.grid(row=0,column=0)
#myLabel2.grid(row=1,column=0)

#Creating Buttons
myButton=Button(root,text="Enter Your Name" ,padx=20,pady=20,command=myClick,fg="blue",bg="Yellow")

#Showing it onto the screen
myLabel1.pack()
myLabel2.pack()
myButton.pack()
e.pack()

root.mainloop()
