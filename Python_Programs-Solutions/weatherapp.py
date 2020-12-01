# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:57:36 2020

@author: DELL
"""
#docs.airnow.api
#u:sunandanaik

from tkinter import *
from PIL import ImageTk,Image
import requests
import json

root=Tk()
root.title('Learn to Code in GUI App')
root.geometry("400x50") #set size of root window


#https://docs.airnowapi.org/CurrentObservationsByZip/docs
#Your API Key: 5C0068DE-5506-438E-8AEE-616FB1C4127C
# https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=20002&distance=25&API_KEY=5C0068DE-5506-438E-8AEE-616FB1C4127C

#Create ziplookup function
def ziplookup():
    zip.get()
    ziplabel=Label(root,text=zip.get())
    ziplabel.grid(row=1,column=0,columnspan=2)



api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=403001&distance=25&API_KEY=5C0068DE-5506-438E-8AEE-616FB1C4127C")
api=json.loads(api_request.content)
city=api[0]['ReportingArea']
quality=api[0]['AQI']
category=api[0]['Category']['Name']
try:
   # api_request=requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=text/csv&zipCode=403001&distance=25&API_KEY=5C0068DE-5506-438E-8AEE-616FB1C4127C")
   # api=json.loads(api_request.content)
   # city=api[0]['ReportingArea']
   # quality=api[0]['AQI']
   # category=api[0]['Category']['Name']
    
    if category == "Good":
        weather_color="blue"
    elif category == "Moderate":
        weather_color="yellow"
    elif category == "Unhealthy for Sensitive Groups":
        weather_color="Orange"
    elif category == "Unhealthy":
        weather_color="Red"
    elif category == "Very Unhealthy":
        weather_color="Violet"
    elif category == "Hazardous":
        weather_color="Brown"
    
    root.configure(background=weather_color)
    
    mylabel=Label(root, text=city +" Air Quality "+str(quality)+ " "+category,font=("Helvetica",20),background=weather_color)
    mylabel.pack()
except Exception as e:
    api="Error..."
    
zip=Entry(root)
zip.grid(row=0,column=0)

zipButton=Button(root,text="Lookup Zipcode", command=ziplookup)
zipButton.grid(row=0,column=1)

root.mainloop()