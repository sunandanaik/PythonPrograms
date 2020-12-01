# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 12:16:53 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image
import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt


root=Tk()
root.title('Learn to Code in GUI App')
root.geometry("400x200") #set size of root window

def graph():
    house_prices = np.random.normal(200000,25000,5000)
    plt.hist(house_prices,50)
    plt.show()


my_btn=Button(root,text="Graph It!",command=graph)
my_btn.pack()

root.mainloop()