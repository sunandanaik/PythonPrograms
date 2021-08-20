# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 17:40:21 2021

@author: DELL


import random as r
import math

num=r.randint(1, 10)
#print(num)

result=r.randrange(10,20,3)
#print(result)

result=math.ceil(r.random())
print(result)

import builtins
print(dir(builtins))

import random as r
channellist=["Aaj Tak", "Sony BBC","Star Plus","Zee"]
item=r.choice(channellist)
print(item)

numbers=[12,23,45,67,65,43]
r.shuffle(numbers)
print(numbers) 

import os
print(os.getcwd())
#os.mkdir("D:\Demo")
#print("Directory Created")
#os.chdir("D:\Python_Tutorial\Python_Programs-Solutions\Batch-3")
#print(os.getcwd())
#print(os.listdir("D:\Demo"))
#os.rmdir("D:\Demo")
#print("Directory has been deleted")
#os.makedirs("this/that")
#print("Directory Created")
#os.rename("C:/Users/DELL/Desktop/Course-Schedule.txt", "C:/Users/DELL/Desktop/Courses.txt")
#print("Rename done!!!")
#print(os.environ.get('Path'))
print(os.path.join("C://", "Testdir"))
print(os.path.exists("D:\Python_Tutorial\Python_Programs-Solutions\Batch-3\Testdir"))

import math
print(math.pi)

import calendar
result=calendar.monthcalendar(2021, 7)
print(result)
for m in calendar.month_name:
    print(m)
    
for d in calendar.day_name:
    print(d)
    
for month in range(1,13):
    mycal=calendar.monthcalendar(2021, month)
    week1=mycal[0]
    week2=mycal[1]
    if week1[calendar.MONDAY] !=0:
        auditday= week1[calendar.MONDAY]
    else:
        auditday= week2[calendar.MONDAY]
    print(f"{calendar.month_name[month]} {auditday}")
    
yy=2021
mm=7
print(calendar.month(yy, mm))
print (calendar.calendar(2021, 2, 1, 6))

#Importing Custom module
#import Testdir.myfunctions as func
#OR
from Testdir import myfunctions as func

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("Division is:",func.divide(a,b))

print("Addition is:",func.addition(a,b))

import sys
#print("You entered: ",sys.argv[0],sys.argv[1],sys.argv[2],sys.argv[3])


print(sys.version)

#print(sys.builtin_module_names)
print(len(sys.argv))
print(sys.stdout.write("Hello Parth!!"))
print(sys.maxsize)
print(sys.path)

import statistics
import math
print("Mean is:",statistics.mean([1,2,3,4,4]))
print("Mean is:",statistics.mean((1,2,3,4,4)))
print("Median is :",statistics.median([42, 21, 34, 65, 90, 45, 109]))
print("Mode is:",statistics.mode({3, 3, 6, 9, 15, 15, 15, 27, 27, 37, 48}))
print("Mode is:",statistics.mode([3, 3, 6, 9, 15, 15, 15, 27, 27, 37, 48]))
print("Mode is:",statistics.mode((3, 3, 6, 9, 15, 15, 15, 27, 27, 37, 48)))
print("Standard Deviation is:", math.floor(statistics.stdev([2,4,4,4,5,5,7,9])))

import collections

emp=collections.namedtuple('employee', ['name','eid','age','salary','dept'])
e1=emp('Parth',101,25,67000,'IT')
e2=emp("John",102,36,56000,'Sales')

print(e1.name) #Parth
print(e1.age)
print(f"Welcome {e1.name},Your employee ID is :{e1.eid} and you are {e1.age} years old. You are posted in {e1.dept}.")
#OR by accessing using index value
print(e1[3])
print(e2[0])
d1={"A":66,"B":89,"C":56}
print(d1)
for i in d1.items():
    print(i)

d2=collections.OrderedDict()
d2["A"]=66
d2["B"]=89
d2["C"]=56
print(d2)
for k,v in d2.items():
    print(f"Student {k} has Scored {v}.")
   
#Collections module-deque()
import collections

q = collections.deque([10,20,30,40,50])
q.appendleft(100)
print(q)

#q.append(200)
#print(q)

#to remove- popleft() & pop()
q.pop()
print(q)
 
for i in range(50):
    print(i)

import time   
i=0
while i<50:
    print(f"{i} - hello")
    time.sleep(1)
    i+=1
 
import time 
a = time.time()
#print(a)
# Get the epoch
#obj = time.gmtime(0)
#print(obj)
#epoch = time.asctime(obj)
#print("epoch is:", epoch)

i=0
while i<50:
    print(f"{i} - hello")
    i+=1
print("While loop ran in :",time.time()-a, "seconds.")


b = time.time() 
for i in range(50):
    print(i)
print("For loop ran in :",time.time()-b,"seconds.")

import time
localtime= time.asctime(time.localtime(time.time()))
print(localtime)

import requests
url="https://httpbin.org/post"
d={'key1':'value1'}
r=requests.post(url=url,data=d)
print(r.text)
#print(r.json())

url="https://www.facebook.com"
d={"somekey":"somevalue"}
r=requests.post(url=url,data=d)
print(r.text)

url = 'https://httpbin.org/get'

x = requests.get(url)
print(x.status_code) #200
print(x.text)
print(x.url)
print(x.headers['Content-Type'])
print(x.cookies)
print(x.json())

mydata = { 'key1': 'value1', 'key2': 'value2'}
x = requests.get(url,params=mydata)
print(x.url)


mydata = { 'key1': 'value1', 'key2': 'value2'}
url = 'https://httpbin.org/post'
x = requests.post(url, data = mydata)
print(x.text)


url = 'https://httpbin.org/post'
data = open('C:/Users/DELL/Desktop/Courses.txt', 'rb')
mydata = {'key1': data}
x = requests.post(url, data = mydata)
print(x.text)
print(x.json())

#JSON module
import json

data = '{"var1":"harry","var2":56}'
result=json.dumps(data)
print(result)
print(type(result))

#dumps() converts python objects into json string object
python_object = ['Hello', 'from', 'AskPython', 42]
 
json_object = json.dumps(python_object)
 
print(type(json_object), json_object)

dict_obj = ["Max","John","Bob","Bill"]
 
json_obj = json.dumps(dict_obj, sort_keys = True, indent = 4)
 
print(json_obj)
print(type(json_obj))

import json

#python_object = ['Hello', 'from', 'AskPython', 42]
json_object = {
    "name": "John",
    "age": 42,
    "married": True,
    "qualifications": ["High School Diploma", "Bachelors"]
}
with open("demo.json","a") as f:
    json.dump(json_object ,f,indent=4)
print("Successfully written into the file")
"""
import json
"""
#dumps() converts from python data into json object
python_object = ['Hello', 'from', 'AskPython', 42]
encoded_object = json.dumps(python_object)
print(encoded_object,type(encoded_object))

#loads() converts from json data into python object
decoded_object = json.loads(encoded_object)
print(type(decoded_object), decoded_object)


python_object = ['Hello', 'from', 'AskPython', 42]
encoded_object = json.loads(python_object)
print(encoded_object,type(encoded_object))

#load() to read from the file

with open("demo.json","r") as f:
    data=json.load(f)
print(data)

#Use pickle module
import pickle

#pickling
cars=["Audi","Bmw","Ferrari","Maruti","Honda"]

file="mycar.pkl"
f=open(file,"wb")
pickle.dump(cars,f)
f.close()
print("Your data is written successfully into the file.")
"""
#depickling
import pickle
f=open("mycar.pkl","rb")
data=pickle.load(f)
print(data)
print(type(data))



















