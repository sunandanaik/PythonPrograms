# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:03:00 2021

@author: DELL
"""
'''
#While Loop to Print first 10 numbers
a=1
while a<=10:
    print(a,end=" ")
    a+=1
print() 
for i in range(1,11):
    print("i = ",i)
    
num=int(input("Enter the Number:"))
for i in range(1,11):
    #print(num,"*",i,"=",num*i)
    print(f"{num} * {i} = {num*i}")
   
#while loop multiplication table
num=int(input("Enter the Number:"))
i=1
while i<=10:
    result=num * i
    print(f"{num} * {i} = {result}")
    i+=1

num=1
sum=0
print("Enter the Number.Please enter zero(0) to exit")
while num!=0:
    num=int(input("Enter Number:"))
    sum=sum+num
    print("Sum =",sum)
    if num <0:
        break
#else:
    #print("Finished!!")
print("Out!!")
 
for i in range(1,11):
    if i==5:
        continue
    print(i)
    

for i in range(1,11):
    if i % 2 != 0:
        continue
    else:
        print(i)
        
l1=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(l1):
    l1[i]=l1[i]+5000
    print(l1[i])
    i+=1
    
A=[0,1,2,3,4,5]  
for i in A:
    print(i)
    
B=(0,1,2,3,4,5)   
for j in B:
    print(j)
    
C={0,1,2,3,4,5} 
for s in C:
    print(s)
    
D='india 012345'
for x in D:
    print(x)

E={"Tom":34,"Max":23,"Bob":12,"Kevin":90}
for n,a in E.items():
    print("Name=",n,", Age=",a)
    
list1=[["Harry",1],["Larry",2],["Carry",6],["marie",250]]
for i,l in list1:
    print(i ," =lollipops:",l)
    
d=dict(list1)
print(d)
for n,l in d.items():
    print("I am ",n," and I have ",l," lollipop(s).")
    
for name in ["Juhi","Sai","Pakhi"]:
    print("Hi",name," Please come to my Party!!")
    
l1=["orange","blue","red","green","purple"]
l2=["chair","sky","apple"]

for c in l1:
    for o in l2:
        print("It is ",c," ",o)
        
result=zip(l1,l2)
print(list(result))

for i in range(1,6):
    for j in range(1,6):
        print(" * ",end="")
    print("\n")
    
for i in range(1,6):
    for j in range(1,i): #range(1,2)
        print(" *",end="")
    print("\n")
  
lst=[]
for x in range(555,1111):
        if(x%7 == 0):
            lst.append(x)
        else:
          print("Finished")
print(lst)
print(len(lst))


items=[int,float,"Harry",5,3,3,22,21,64,23,233,23,6,6.7]
for item in items:
      if str(item).isnumeric() and item >=6:
          print(item)
          print(str(item))

#To search for lost car key in home and when found stop searching
key_location ="kitchen"
locations=["garage","living room","chair","closet","kitchen","Drawing room","bedroom"]
for i in locations:
    if i==key_location:
        print("key is found in ",i)
        break #comes out of for loop
    else:
        print("Key is not found ",i)
        continue
     
#To find square of numbers from 1 to 5 except for even numbers
for i in range(1,6):
    if i%2 == 0:
        continue
    else:
       print(i*i)
       
i=1
while i<6:
    if i%2 ==0:
        continue
    else:
        print(i*i)
 

i=0
while(True):
    print(i+1, end=",")
    if i==44:
        break
    else:
       i=i+1
       
i=0
while(True):
      if i+1 <5:
          i=i+1
          continue
      else:
         print(i+1)
         if(i==44):
             break # stop the loop
         else:
             i=i+1    

#print("wjnsdflkskvdl;fbdfvdfbdfb \n dfdfvdkf klvkdlfvdfv") 
while(True):
  n=int(input("Enter a number:"))
  if n>100:
     print("Congrats, you have entered a number greater than 100\n")
     break
  else:
     print("Try again!!\n")
     continue

print("How many rows you want to print ?:")
n =int(input("Enter row size:"))
print("Type 1 or 0");
ch=int(input("Enter choice:"))
b=bool(ch)
if b== True:
    for i in range(1, n+1): #range(1,6)
        for j in range(1, i+1): #range(1,6)
            print("*",end="")
        print()
elif b==False:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()

print("How many rows you want to print:")
n=int(input()) #5
print("Type 1 or 0")
ch=int(input())
b=bool(ch)
if b ==True:
   for i in range(0,n+1): #range(0,6)
        print("*" * i) # * x 5 = *****
        
if b==False:
     for i in range(n,0,-1): #range(5,0,-1)
        print("*" * i) # * x 1 = *
'''        
#Using else with for loops
khana=["roti","sabji","chawal","rotiroll"]
for item in khana:
    if item=="rotiroll":
        print("I found it")
        break
    # if item=="paratha":
    #     break
    # print(item)
    # break
else:
    print("this for loop ended properly")




            



    

    