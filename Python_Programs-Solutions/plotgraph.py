from tkinter import *
from PIL import ImageTk,Image
import numpy as np
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

print("hi")

root=Tk()
root.title('Learn to Code in GUI App')
root.geometry("400x200") #set size of root window

def graph():
    house_prices = np.random.normal(200000,25000,5000)
    plt.polar(house_prices)
    plt.show()


my_btn=Button(root,text="Graph It!",command=graph)
my_btn.pack()

root.mainloop()