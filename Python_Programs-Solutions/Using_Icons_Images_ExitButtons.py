# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 19:45:44 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("Learn to Code in Tkinter GUI App")

#to display icon of tkinter app
root.iconbitmap('d:/Pictures/python.ico')

#to display list of images
my_img1=ImageTk.PhotoImage(Image.open("d:/Pictures/running2.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("d:/Pictures/python.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("d:/Pictures/oldman.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("d:/Pictures/paper.png"))
my_img5=ImageTk.PhotoImage(Image.open("d:/Pictures/motorola.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5]
#image_list[2]

#Adding status bar
status=Label(root,text="Image 1 of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)#bd is border

my_label=Label(image=my_img1)

#Forward button function
def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))
    
    if image_number==5:
        button_forward=Button(root,text=">>",state=DISABLED)
    
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)
    my_label.grid(row=0,column=0,columnspan=3)
    
    status=Label(root,text="Image "+ str(image_number)  +" of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)#bd is border
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)
    

#Back Button function
def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label=Label(image=image_list[image_number-1])
    button_forward=Button(root,text=">>",command=lambda:forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))
    
    if image_number==1:
        button_back=Button(root,text="<<",state=DISABLED)
    
    button_forward.grid(row=1,column=2)
    button_back.grid(row=1,column=0)
    my_label.grid(row=0,column=0,columnspan=3)
    
    status=Label(root,text="Image "+ str(image_number)  +" of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)#bd is border
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)


button_back=Button(root,text="<<",command=back,state=DISABLED)
button_quit=Button(root,text="Exit Program",command=root.quit)
button_forward=Button(root,text=">>",command=lambda:forward(2))


my_label.grid(row=0,column=0,columnspan=3)
button_back.grid(row=1,column=0)
button_quit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=10)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

root.mainloop()