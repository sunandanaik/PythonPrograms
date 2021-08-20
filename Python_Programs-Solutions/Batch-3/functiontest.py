# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:16:12 2021

@author: DELL

print("Good evening Parth")
print("Good evening Kevin")
print("Good evening Max")

#Function Example-1
#Function definition/creation
def greetingName(name):
    
    print("Good evening ", name)
    
def test():
    
    print("Hello world!!") 
    
#function calling
#Driver's code
greetingName("Parth")
greetingName("Kevin")
greetingName("Max")
greetingName("Bob")
greetingName("Steve")
print(test.__doc__)
print(greetingName.__doc__)

sum=0#global variable
a=20
b=30
def addition(a,b):
    sum=a+b
    print("The Sum is:",sum)

def subtraction(a,b):
    sub=a-b
    print("The difference is :",sub)

addition(1,2)
subtraction(4,7)

#Function with return example

def greetUser(name):
    return "Hello " +name

n1=greetUser("Parth")
print(n1)
n2=greetUser("Steve")
print(n2)
n3=greetUser("Kevin")
print(n3)

def addnum(num):
    return num+100

n=addnum(10)
print(n)

print(addnum(20))

def my_add(a:int,b:int)->int:
    return (a+b)

def my_add2(a,b):
    return(a+b)

print(my_add(40,60))
print(my_add2(40,40))

#Function with default argument using dictionary
studentlist={11:"Steve", 12:"Mark", 13:"Parth", 14:"Bob", 15:"Smith"}

def printName(rollno):
    return f"Hi {studentlist.get(rollno,'Unknown')} !!"

print(printName(100))

#Call by value
name="Steve"
def Demo(name):
    name="Parth"
    print("Hi ",name)

Demo("Mark")
print("Outsider name:",name)

#Call by reference

def addlist(mylist):
    mylist.append(60)
    print("Inside the function :",mylist)
    
    
mylist=[10,20,30,40,50]
addlist(mylist)
print("Outside the function:",mylist)

def swapnum(a,b):
    temp=a
    a=b
    b=temp
    print("After swapping , the values in a and b are:",a," and ",b)

a=[10]
b=20
print("Before swapping , the values in a and b are:",a," and ",b)
swapnum(a,b) #copy i.e.pass by value
print("After swapping outside function , the values in a and b are:",a," and ",b)


def editlist(l):
    l.append(30)
    print("inside function:",l) #[10,20,30]


a=[10,20]
editlist(a) #address i.e. pass by reference
print("outside function:",a) #[10,20,30]

def set_list(l):
    result=l+5
    #l=["A"]
    #l.append("A")
    #print(l)
    return result
#end of function

#Drivers code (main code)
list1=10
a=set_list(list1)
print(a)

def func1():
    global x
    print("x1:",x) #parth
    x="steve"
    print("inside function:",x) #steve
    
x="parth"
func1()
print(x) #steve


def func2():
    b=50
    print("Func2 :",b) #50
    def inner():
        nonlocal b
        b=100
        print("Inner func:",b) #100
    inner()
    print("Func2 :",b) #100
    

b=20
func2()
print("Outside func2:",b) #20


#Create simple calculator using function
def calculatorfunc(operator,a,b):
    if operator == '+':
        #print("Addition is: ",a+b)
        
        return a+b
    elif operator=='-':
        print("Difference is ",a-b)
    elif operator=='*':
        print("Multiplication is:",a*b)
    elif operator=='/':
        print("Division is:",a/b)
    else:
        print("Invalid operator!!")
        

calculatorfunc('-',10,20)
calculatorfunc('*',10,20)
calculatorfunc('/',10,20)
calculatorfunc('%',10,20)

#Recursion
def checkage(age):
    if age>=18:
        print("You are eligible!!")
        print("Enter Age:")
        age=int(input())
        checkage(age) #function calling
    else:
        print("You are not eligible!!")
    
checkage(20) #function calling


#Calculating factorial of number using recursion of function
def factorial(n):
    if n!=0:
        return (n * factorial(n-1)) #5 * 4 * 3 * 2 *1 * 1
        
    else:
        return 1


a=int(input("Enter the number:"))
while (a>0):
    print(factorial(a))#function calling
    a=int(input("Enter the number:"))

#Fibonacci Series using recursion (0,1,1,2,3,5)
def fibo(a):
    if a<=1:
        return a
    
    else:  
        #print(fibo(a))
        return (fibo(a-2) + fibo(a-1)) #fibo(4)+fibo(3)
        
        

fibolist=[]
a=int(input("Enter the number:")) #a=5
if a<=0:
    print("Please enter positive number only")
else:
    for i in range(0,a): #(0,5)
        #print(fibo(i)) #0,1,1,2,3
        fibolist.append(fibo(i))
    print(fibolist)

def student(name,age,**marks):
    print("Name is :",name)
    print("Age is :",age)
    for name,value in marks.items():
        print(name ,":",value)
    
student("Parth",20,Python=90,C=89,Cpp=78,Java=89)

def printNames(*names):
    for n in names:
        print(n)
    
namelist=["Harry","Parth","Kevin","Bob","Anna","Pooja","Bill","Rajesh","Rakesh"]
#printNames(namelist)

#OR
var1=printNames
var1(namelist) #function calling

def Demo():
    print("I am demo function!!!")
    
#print("Hello Parth",Demo)
#datalist=["Hello Parth",Demo]
#datalist[1]()
#print(datalist[0])

#As dictionary key
dict={Demo:Demo()}
dict[Demo]

def inner():
    print("I am inner function!!")
    
def outer(a):
    a(namelist)

#Drivers Code
#outer(inner) #function calling-1
#outer(Demo) #function calling-2
outer(printNames) #function composition


def student(*names,**heroes):
    for n in names:
        print(f"Names are:{n}") #print("marks are:",n)
    for key,value in heroes.items():
        print(f"{key}:{value}")

student("Parth","Bob",Monitor="Steve",Coordinator="Smith",Coder="Parth")


    
def add(a,b):
    print(a+b)
    def printresult():
        print("I am print result function")
    #print(result)
    
    return printresult #return None value

#print(add(5,4)) #function caling
var1=add
var1(2,3)()#function caling

#Use of sorted()
names=["Parth","Steve","Kevin","Anna"]
print(sorted(names))
marks=[56,34,78,12]
print(sorted(marks))

#Callback function
def display():
    print("This is display function")
    
def add(a,b,display):
    print(a+b)
    display() #callback function
       
add(2,3,display)

names=["Parth","Steve","Kevin","Anna"]
print(sorted(names,reverse=True))


def calculatesq(n):
    result=n*n
    print("Square is :",result)

calculatesq(3)

#Lambda function Example
result= lambda n : n*n

n=int(input("Enter the number for n:"))
print("Square is :",result(n))

def addnum(a,b):
    result=a+b
    #print("Addition is:",result)
    return result

sum=addnum(2,3)
print("Sum is :",sum)

result=lambda a,b : a+b
print("Sum is:",result(2,3))

ans=lambda str:str[ : : -1]
print(ans("Parth is a good boy"))

def revstr(name):
    result=name[::-1]
    return result

print(revstr("Parth is a good boy"))


print((lambda str:str[ : : -1])("Parth is a good boy"))
#print(ans)



def avgfunc(a,b,c):
    avg=(a+b+c)/3
    print("Average:",avg)

avgfunc(10,20,30)

#Lambda without parameters
ans=lambda : "Parth"
print(ans())

#OR
print("Sum is:",(lambda : (10+20+30)/3)())

import math
n1=int(input("Enter value for a:"))
n2=int(input("Enter value for b:"))
n3=int(input("Enter value for c:"))
print("Average is :",(lambda a,b,c : math.ceil((a+b+c)/3))(n1,n2,n3))

#Calculator with return statement
def add(a,b):
    c=a+b
    return c

def subtract(a,b):
    c=a-b
    return c

def multiply(a,b):
    c=a*b
    return c

def divide(a,b):
    c=a/b
    return c

def getOperationNo(choice):
    if choice == 1:
        return add
    elif choice==2:
        return subtract
    elif choice==3:
        return multiply
    elif choice==4:
        return divide

#Drivers Code
while (True):
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 0 for Exit")
    
    choice=int(input("Enter your choice no:"))
    if (choice==0):
        break
    
    else:
        var=getOperationNo(choice) #function calling var=subtract
        a=int(input("Enter value for a:"))
        b=int(input("Enter value for b:"))
        result=var(a,b)
        print("Result is :",result)
print("Thank You. Visit Again")


def sortlist(lst):
    return lst[1]

lst=[[1,14],[5,6],[8,23]]
lst.sort(key=sortlist)
print(lst)

#Using lambda
lst=[[1,14],[5,6],[8,23]]
lst.sort(key=lambda l : l[1])
print(lst)

def demo(x):
    print("I am returning multiple values")
    return x,x*3,x+5

#drivers code
var=demo(10)
print(var)

#Using lambda
var=lambda x: (x,x*3,x+5)
print(var(3))
#OR
print((lambda x: [x,x*3,x+5])(3))

#OR
print((lambda x: {1:x , 2 : x*3 , 3: x+5})(3))

#Using filter()
numlist=[1,2,3,4,5,6,7,8,9]
result =tuple(filter(lambda n : n>5 ,numlist))
print(result)

animals=["cat","Cat","CAT","emu","Emu","EMU"]

def checkupper(s):
    return s.isupper()

result= list(filter(checkupper, animals)) #function call
print(result)

#Using lambda with filter
result= list(filter(lambda s : s.isupper(),animals))
print(result)

l1=[87,56,45,23,12]
result= list(filter(lambda x : (x%2==0), l1))
print(result)

l1=[87,56,45,23,12]
result=list(filter(lambda x : True if x > 45 else False, l1))
print(result)

def check45(x):
    if x>45:
        return True
    else:
        return False
    
result= list(filter(check45, l1))
print(result)

def reversestring(s):
    return s[: : -1] #elppa

#result = reversestring("Hello Python")
#print(result)

fruits=["apple","banana","grapes","plum","orange"]
for f in fruits:
    print(reversestring(f)) #function calling
    
#Using map()
print(list(map(reversestring,fruits)))
#print(result)

marks=[89,78,67,90,100]
print(marks)

#using for loop
for m in marks:
    print(m)
    
#using map()
def printmarks(m):
    return m

result=list(map(printmarks, marks))
print(result)


#Map() function
numbers=["3" ,"30", "89" , "45"]
#to convert string items into int items in list

print(numbers)
#print(len(numbers))
#using for loop

for i in range(len(numbers)):  #for i in range(0,4):
    numbers[i]=int(numbers[i])  #"3" -> 3
    print(numbers[i])
    numbers[i]=numbers[i] + 100
    print(numbers[i])

    
#map() function
print(list(map(int, numbers)))

#To find square of all the numbers in list using map():
lst=[1,2,3,4,5,6,7,8,9]
def squarenum(a):
    return a*a

#print(list(map(squarenum , lst)))
#using for loop
for i in range(0,len(lst)):
    print(squarenum(lst[i])) #function calling
    

def square(a):
    return a*a

def cube(a):
    return a*a*a

lst=[square, cube]

num =int(input("Enter  a number:")) #4

print(list(map(lambda func : func(num), lst)))

 #func=square
 #func(num) #func(4)
  #func=cube
#func(num)  

#Using join function
lst=["apple","orange","grapes"]
#lst=[1,2,3,4,5]
print("-".join(lst))
print(lst)

#Since join() accepts string list and not int list, so use loop
fruitlist=[] #empty list ["10","20","30","40","50"]
numlist=[10,20,30,40,50]
for i in numlist:
    fruitlist.append(str(i)) #"10"
print(fruitlist)
print("-".join(fruitlist))  

#Alternatively using map()

print("/".join(map(str,numlist)))

l1=[1,2,3] #3
l2=[10,20,30] #3
l3=[100,200,300] #3
l4=[11,22,33]

def addlist(a,b,c,d):
    return (a+b+c+d)

#using loop
for i in range(0,len(l3)): #range(0,3)
    print(addlist(l1[i],l2[i],l3[i],l4[i]))
    
#using map()
print(list(map(addlist, l1,l2,l3,l4)))

l1=[1,2,3] #3
l2=[10,20,30] #3
l3=[100,200,300] #3
l4=[11,22,33]
#using map with lambda
print(list(map((lambda a,b,c,d : a+b+c+d) , l1,l2,l3,l4)))
    
lst=[1,2,3,4,5,6,7,8,9]
lst2=[10,20,30,40,50,60]
def addnum(a,b):
    return a+b

print(list(map(addnum , lst,lst2)))

#reduce()
from functools import reduce
print(reduce(addnum,lst))

#reduce with lambda
print(reduce(lambda a,b: a+b , lst))

#using loop
sum=0
for i in lst:
    sum=sum+i #sum+=i
print(sum)

#Example
from functools import reduce
#lst=[1,2,3,4,5,6,7,8,9]
def multiplynum(a,b):
    return a*b

def printresult(n):
    return reduce(multiplynum, range(1,n+1))

n=int(input("Enter the limit:"))    #50
result=printresult(n)
print(result)

from math import factorial
n=int(input("Enter the limit:")) 
print(factorial(n))

#Using accumulate() with lambda
import itertools as it
list1=[10,20,30,40,50]

def addnum(a,b):
    return a*b
print(list(it.accumulate(list1, addnum)))
#print(list(it.accumulate(list1, lambda a,b:a+b)))

shoplist=["Tomato","Potato","Grapes","Orange"]
#print(shoplist[0]) #tomato indexvalue=0

indexvalue=1
for item in shoplist: #[0]
    if indexvalue==1:
        print(item,"Buy it")
    elif indexvalue%2 == 0:
        print(item ,"Please buy it")
    else:
        print(item," Dont buy it")
    indexvalue+=1
    
#Using enumerate()
shoplist=["Tomato","Potato","Grapes","Orange"]

for indexvalue, item in enumerate(shoplist):
    if indexvalue==0:
        print(item,"Buy it")
    elif indexvalue%2 == 0:
        print(item ,"Please buy it")
    else:
        print(item," Dont buy it")
        
"""
#Using join()
shoplist=["Tomato","Potato","Grapes","Orange"]

for i in shoplist:
    print(i,end=":")
    
#OR
print()
result=":".join(shoplist)
print(result)
    





    

    
    
    
    




    






    

