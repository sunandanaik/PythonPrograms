import time
import tkinter
from turtle import width
import PIL.Image,PIL.ImageTk #pip install pillow
import cv2 #pip install opencv-python
from functools import partial
import threading

from matplotlib.pyplot import flag
import imutils

#width and height of main screen
SET_WIDTH = 650
SET_HEIGHT = 368

#tkinter gui starts here
window = tkinter.Tk()
window.title("Third Umpire Decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread('Images/drswelcome.jpg'),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0,0,anchor=tkinter.NW,image=photo)
canvas.pack()

stream = cv2.VideoCapture('clip.mp4')
flag=True
#Button functions
def play(speed):
    global flag
    print(f"You clicked on play with Speed of {speed}")
    
    #play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)
    grabbed,frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(132,20,fill="black",font="Times 25 bold", text="Decision Pending")
    flag= not flag


def pending(decision):
    #display decision pending image
    frame = cv2.cvtColor(cv2.imread("Images/decisionpending.jpg"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #wait for 1 second
    time.sleep(1)
    #display sponsor image
    frame = cv2.cvtColor(cv2.imread("Images/decision.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    #wait for 1.5 seconds
    time.sleep(1.5)
    #display out/not out image
    if decision == 'out':
        decisionImg="Images/out.PNG"
    else:
        decisionImg="Images/notout.PNG"
    frame = cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    


def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is Out!!")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is Not Out !!")

#Buttons to control playback
btn1 = tkinter.Button(window,text="<< Previous (fast)",width=50,command=partial(play,-25))
btn1.pack()
btn2 = tkinter.Button(window,text="<< Previous (slow)",width=50,command=partial(play,-2))
btn2.pack()
btn3 = tkinter.Button(window,text="Next (fast) >>",width=50,command=partial(play,25))
btn3.pack()
btn4 = tkinter.Button(window,text="Next (slow) >>",width=50,command=partial(play,2))
btn4.pack()
btn5 = tkinter.Button(window,text="Give Out",width=50,command=out)
btn5.pack()
btn6 = tkinter.Button(window,text="Give Not Out",width=50,command=not_out)
btn6.pack()

window.mainloop()