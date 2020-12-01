# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:23:36 2020

@author: DELL
"""

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

root=Tk()
root.title('Learn to Code in GUI App')
root.geometry("400x400") #set size of root window

#Databases
#Create a database or connect to one
conn=sqlite3.connect('D:/Python_Tutorial/Python_Programs-Solutions/address_book.db')

#create cursor
cur = conn.cursor()

#Create Save button function for editor screen
def save():
    #Create a database or connect to one
    conn=sqlite3.connect('D:/Python_Tutorial/Python_Programs-Solutions/address_book.db')
    
    #create cursor
    cur = conn.cursor()
    
    record_id=delete_box.get()
    cur.execute(""" UPDATE addresses SET
                first_name =:first,
                last_name=:last,
                address=:address,
                city=:city,
                state=:state,
                zipcode=:zipcode
                
                WHERE oid= :oid""",
                {
                'first':f_name_editor.get(),
                 'last':l_name_editor.get(),
                 'address':address_editor.get(),
                 'city':city_editor.get(),
                 'state':state_editor.get(),
                 'zipcode':zipcode_editor.get(),
                 'oid':record_id
                })
    
     #Clear the text boxes
    f_name_editor.delete(0,END)
    l_name_editor.delete(0,END)
    address_editor.delete(0,END)
    city_editor.delete(0,END)
    state_editor.delete(0,END)
    zipcode_editor.delete(0,END)
    
    #Commit changes
    conn.commit()
    
    #Close db connection
    conn.close()
    
    editor.destroy()
#end of save function

#Create update funtion to update record
def update():
    global editor
    editor=Tk()
    editor.title('Update A Record')
    editor.geometry("400x400") #set size of root window
    
    #Create a database or connect to one
    conn=sqlite3.connect('D:/Python_Tutorial/Python_Programs-Solutions/address_book.db')
    
    #create cursor
    cur = conn.cursor()
    
    record_id=delete_box.get()
    
    #To query the database
    cur.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records=cur.fetchall()
    
   
    #Create global variables for textbox names
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor
    
    #Create textbox labels

    f_name_label=Label(editor,text="First Name")
    f_name_label.grid(row=0,column=0,pady=(10,0))
    
    l_name_label=Label(editor,text="Last Name")
    l_name_label.grid(row=1,column=0)
    
    address_label=Label(editor,text="Address")
    address_label.grid(row=2,column=0)
    
    city_label=Label(editor,text="City")
    city_label.grid(row=3,column=0)
    
    state_label=Label(editor,text="State")
    state_label.grid(row=4,column=0)
    
    zipcode_label=Label(editor,text="Zipcode")
    zipcode_label.grid(row=5,column=0)
    
   
    #Create textboxes
    
    f_name_editor=Entry(editor,width=30)
    f_name_editor.grid(row=0,column=1,padx=20,pady=(10,0))
    
    l_name_editor=Entry(editor,width=30)
    l_name_editor.grid(row=1,column=1,padx=20)
    
    address_editor=Entry(editor,width=30)
    address_editor.grid(row=2,column=1,padx=20)
    
    city_editor=Entry(editor,width=30)
    city_editor.grid(row=3,column=1,padx=20)
    
    state_editor=Entry(editor,width=30)
    state_editor.grid(row=4,column=1,padx=20)
    
    zipcode_editor=Entry(editor,width=30)
    zipcode_editor.grid(row=5,column=1,padx=20)
    
    
     #Loop trhu results
    for record in records:
        f_name_editor.insert(0,record[0])
        l_name_editor.insert(0,record[1])
        address_editor.insert(0,record[2])
        city_editor.insert(0,record[3])
        state_editor.insert(0,record[4])
        zipcode_editor.insert(0,record[5])
    
   #Create Save button
    save_btn=Button(editor,text="Save Record",command=save)
    save_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=137)
    
 #end of update function   
    
    
#Create function to delete record
def delete():
     #Create a database or connect to one
    conn=sqlite3.connect('D:/Python_Tutorial/Python_Programs-Solutions/address_book.db')
    
    #create cursor
    cur = conn.cursor()
    
    #Delete a record
    cur.execute("DELETE FROM addresses WHERE oid="+delete_box.get())
    messagebox.showinfo("Record Deleted Successfully !!!")
    delete_box.delete(0,END)
    
    
    
    
    #Commit changes
    conn.commit()
    
    #Close db connection
    conn.close()
    
    

#Create submit button function
def submit():
    
    #Create a database or connect to one
    conn=sqlite3.connect('D:/Python_Tutorial/Python_Programs-Solutions/address_book.db')
    
    #create cursor
    cur = conn.cursor()
    
    #Insert into Table addresses
    cur.execute("INSERT INTO addresses VALUES(:f_name,:l_name,:address,:city,:state,:zipcode)",
                {
                  'f_name':f_name.get(),
                  'l_name':l_name.get(),
                  'address':address.get(),
                  'city':city.get(),
                  'state':state.get(),
                  'zipcode':zipcode.get()
                })
    
    
    #Clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zipcode.delete(0,END)
    
    
    #Commit changes
    conn.commit()
    
    #Close db connection
    conn.close()
#end of submit function

#Show button function
def show():
    #Create a database or connect to one
    conn=sqlite3.connect('D:/Python_Tutorial/Python_Programs-Solutions/address_book.db')
    
    #create cursor
    cur = conn.cursor()
    
    #To query the database
    cur.execute("SELECT *,oid FROM addresses")
    records=cur.fetchall()
    #print(records)
    
    #Loop through Results
    print_records=''
    for rec in records:
        print_records += str(rec[0])+" "+str(rec[1])+" "+str(rec[2])+" "+str(rec[3])+" "+str(rec[4])+" "+str(rec[5]) +" "+" \t"+str(rec[6])+"\n"
        
    query_label=Label(root,text=print_records)
    query_label.grid(row=12,column=0,columnspan=2)
    
    #Commit changes
    conn.commit()
    
    #Close db connection
    conn.close()
#end of show button function

#Create textbox labels

f_name_label=Label(root,text="First Name")
f_name_label.grid(row=0,column=0,pady=(10,0))

l_name_label=Label(root,text="Last Name")
l_name_label.grid(row=1,column=0)

address_label=Label(root,text="Address")
address_label.grid(row=2,column=0)

city_label=Label(root,text="City")
city_label.grid(row=3,column=0)

state_label=Label(root,text="State")
state_label.grid(row=4,column=0)

zipcode_label=Label(root,text="Zipcode")
zipcode_label.grid(row=5,column=0)

delete_box_label=Label(root,text="Select ID Number:")
delete_box_label.grid(row=8,column=0,pady=5)


#Create textboxes

f_name=Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,pady=(10,0))

l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20)

address=Entry(root,width=30)
address.grid(row=2,column=1,padx=20)

city=Entry(root,width=30)
city.grid(row=3,column=1,padx=20)

state=Entry(root,width=30)
state.grid(row=4,column=1,padx=20)

zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=20)

delete_box = Entry(root,width=30)
delete_box.grid(row=8,column=1,pady=5)



#Create submit button

submit_btn=Button(root,text="Add Record To Database", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,padx=10,pady=10,ipadx=100)

#Query button
show_btn=Button(root,text="Show Records",command=show)
show_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

#Create delete button
delete_btn=Button(root,text="Delete Record",command=delete)
delete_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=136)

#Create Update button
update_btn=Button(root,text="Edit Record",command=update)
update_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=145)

#Commit changes
conn.commit()

#Close db connection
conn.close()

root.mainloop()