# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:11:57 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root=Tk()
root.title('Learn to Code in GUI App')
root.geometry("400x400") #set size of root window

#Databases
#Create a database or connect to one
conn=sqlite3.connect('D:/Python_Tutorial/Python_Programs-Solutions/address_book.db')

#create cursor
cur = conn.cursor()

#Create table
cur.execute("""  CREATE TABLE addresses(
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer
             )""")


#Commit changes
conn.commit()

#Close db connection
conn.close()



root.mainloop()