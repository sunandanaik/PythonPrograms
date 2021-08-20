# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:12:01 2021

@author: DELL
"""

print("Hello world!")

"""a=int(input("Enter number for a:"))
b=int(input("Enter number for b:"))
c=a+b
print("c =",c) """

'''s1=input("Enter your firstname :")
s2=input("Enter your lastname :")

s3=s1+s2
print(s3)'''

'''a=float(input("Enter number for a:"))
b=float(input("Enter number for b:"))
c=a*b
print("c =",c)'''

'''
print(bool(True) )
b1=False
print(b1)

x=2
y=5
exp= x+y-(x*x)/y
print(exp)

#Relational Operators
empsal1=45000
empsal2=67000

print(empsal1>empsal2)
print(empsal1<empsal2)
print(empsal1==empsal2)
print(90!=80)
print(23>=23)
print(10<=20)

#Logical Operators
a=10
b=20
c=30

print((a>b) & (a>c))
print((a>=a) | (b>c))
print(not(c>a))

age_student=23


age_student=56
print(age_student)

name='My name is John'

print(name)

print(name[11])
print(name[-1])
print(name[3 : 7])

num=98.8
print(type(num))

s=str(num)
print(name+s)

print("Length of the string is :",len(name))

print("In Lowercase : ", str.lower(name))

print("In Uppercase : ", str.upper(name))
print("In Lowercase : ", str.title(name))

print(name.replace('m', 'f'))
strings="hello hello- good morning,- hope you are good,hello -byebye"
print(strings.count("hello"))
print(strings.find("morning"))
print(strings.split('-'))

string1="data analytics"
print(string1[ 1 :-4 ]) 
print(string1 * 4)
print(string1 + str(5))

tupl1=("John",25,67000.89,"New york","IT")
tupl2=("Kevin",23,56000,"Japan","Sales")

print(tupl1)
print(type(tupl1))
print(tupl1[0])
print(tupl1[-2])
print(tupl1[1 :5 ])


print(len(tupl1))
print(tupl1 + tupl2)
print(tupl1 * 5)
tupl3=(45,67,78,89,45)
print(min(tupl3))
print(max(tupl3))

#List DS
l1=[1, "World","corona",'c',3.14,True]
print(type(l1))
print(l1)
print(l1[2])
print(l1[:])
print(len(l1))
l1[0]="Parth"
print(l1)
l1[5]=False
print(l1)
l1.append(78000)
print(l1)
print(l1.pop())
print(l1)
print(l1.remove("corona"))
print(l1)
del(l1[4])
print(l1)
l2=[1,"a",2,'b',3,"corona",2.5]
#l2.reverse()
#print(l2)
l3=["green","red","black","white","orange"]
#l3.sort()
print(l3)
l4=[34,12,7,90,3.14]
l4.sort()
print(l4)
l2.insert(1, "python")
print(l2)
l3.extend(["silver","grey","blue"])
print(l3)
#Concatenating of lists
print(l2+l3)

print(sorted(l4))
print(l3 *5)

state=["Goa","Bangalore","Mumbai","Delhi","kolkata"]
print("Goa" in state)
print("UP" in state)
print("Delhi" not in state)

print("Copying of list items")
newstate=[]
newstate=state.copy()
print(newstate)
print("-------------------------------------")
tupl1=("John",25,67000.89,"New york","IT")

#tuple doesntnot allow copying of items
#newtup=()
#newtup=tupl1.copy()
#print(newtup)
print("----------------------------")

print(max(l4))
print(min(l4))

#List Comprehension
inlist=[1,2,3,4,5,6,7,8,9,10]

outlist=[ n+5 for n in inlist]
print(outlist)

#Without List Comprehension
outlist2=[]
for n in inlist:
    n=n+5
    outlist2.append(n)
print(outlist2)

#List Comprehension
outlist3=[n*n for n in inlist]
print(outlist3)

#List Comprehension
outlist4=[n for n in inlist if n%2==1]
print(outlist4)

#Without List Comprehension
outlist5=[]
for n in inlist:
    if n%2==0:
        outlist5.append(n)
    else:
        continue
print(outlist5)

outlist6=[ n+5 for n in range(51,61)]
print(outlist6)

#or
for n in range(51,61):
    if n==55:
        continue
    
    else:
        n=n+5
        print(n)
        

for n in range(1,11):
    if n==5:
        break
    else:
        print(n)
        
#Dictionary Example
d1={"Apple":50,"Orange":34,"Grapes":100,"Mango":1000}
print(type(d1))
print(d1)

print(len(d1))

d2={'name':'Tom', 15 : 15, 3.14 : 3.14, True : "On", False:"Off", (2,3):5}
print(d2)
print(d2.items())
print(d2[True]) #On
print(d2[(2,3)]) #5

print(d2.get('name'))
print(d2.get(True))

d2['lname']='DSouza'
print(d2)

d2['name']="Kevin"
print(d2)
d2.clear()
print(d2)

print(d1.keys())
print(d1.values())
d3={'name':'Tom', 15 : 15, 3.14 : 3.14, True : "On", False:"Off", (2,3):5}
d1.update(d3)
print(d1)

newdict={'name':'Tom','lname':'DSouza','age':34,'rollno':11,True : "On",(2,3):5,3.14 : 3.14}
car = {"brand": "Ford","model": "Mustang","year": 1964}
car.update(newdict)
print(car)
car.pop("rollno")
print(car)
car.pop("age",'True') #multiple popping of items not possible
print(car)

#using for loop iterate through dictionary items
for x, y in car.items():
  print(x ," : " , y)
  
#only display values from car dictionary using loop
for v in car.values():
    print("Values =",v)
    
#only keys to display
for k in car.keys():
    print("Keys =",k)
    
print("------------------------------")
for i in car:
    print("Values=",car[i])
    
for j in car:
    print(j," =",car[j])
    
#Membership operator(in & not in)
if "qutub" in car:
    print("Yes, it is present")
else:
    print("No, it doesnt exist.")
    
newcar={}
newcar=car.copy()
print(newcar)
a=[1,2,3]
print(list(a))
c=list(a)
print(c)
print(a==c)
print(a is c)
d=a
print(d)
print(a is d)

newcar.update({"year":2020})
print(newcar)

#Nested Dictionary Example
myfamily={"child1":{"age":12,"class":5}, "child2":{"age":10,"class":6},"child3":{"age":15,"class":9}}
print(myfamily)

x = {'a': 1, 'b': 10}
y = {'b': 15, 'c': 4}
z = {**y, **x}
print(z)

d={"tom":66786858,"Joe":45346456456,"Max":354346464}

for i in d:
    print("Name :",i," = ",d[i])
    
for k,v in d.items():
    print("Name :",k," = ",v)
    
import operator
xs = {'a': 12, 'b': 23, 'c': 26, 'd': 10}
print(sorted(xs.items(), key=operator.itemgetter(1)))

#Dictionary Comprehension Example
cities=["mumbai","paris","chicago"]
countries=["india","france","usa"]
z=zip(cities,countries)
print(z)
#for a in z:
#    print(a)
    
for city, cty in z:
    print(city," is in ", cty)
    
#Dictionary comprehension
d={city:country for city,country in zip(cities,countries)}
print(d)

#Set Examples
s=set()
print(type(s))
print(s)
#s.add([1,2,3,4,5,6,7,8,9,0])
#s.add(2)
#s.add(3)
#s.add(4)
print(s)



st={1,2,5,'a','b','e','a','d','f',5,"parth","india"}
print(st)

st2={1,2,1,2,3,4,5}
print(st2)

st3={1,4,2,4,'aaa','abc',9,2}
print(st3)

lists=[1,4,3,'abc',87,'abc',4,1]
st4=set(lists)
print(st4)
print(type(st4))

st5=set()
lists=[1,2,3,4,5,6,7,8,9,0]

for item in lists:
    st5.add(item)
print(st5)

#Set Comprehension Example
st6=set([1,2,3,4,5,6,5,2,3])
print(st6)
result={i for i in st6 if i%2==0}
print(result)

print(len(st6))

#Accessing elements of set
for e in st6:
    print(e)
    
st7={1,3,4,'abc'}
st7.add(10)
print(st7)

st7.update([11,12,13,14,15])
print(st7)

st8={1,3,4,'abc',87,4}
#st8.remove('abc')
print(st8)
#st8.remove(4)
print(st8)
#st8.discard(200)
print(st8)
#print(st8.pop())
print(st8)
print(st8.pop())
print(st8)

a={1,2,4.6,7.8,'r','s'}
b={2,5,'d','abc'}
print(a | b)
print(a.union(b))

print(a & b)
print(a.intersection(b))

print(a-b)
print(a.difference(b))

print(b-a)
print(b.difference(a))

#Frozen set
st9=frozenset(a)
print(st9)

number1 = 10
number2 = 40
number3 = 30


if number1 < number2:
    print(number1 ," is lesser than ",number2)
else:
    print(number1, " is greater than ",number2)
    
a=30
b=25
c=18



#if-else ladder structure
if a>b and a>c:
    print("a is the eldest no")
elif b>a and b>c:
    print("b is the eldest no")
elif c>a and c>b:
    print("c is the eldest no")
    
#Nested if-else structure
if a>b:
    if a>c:
        print("a is the eldest no")
    else:
        if c>b:
           print("c is the eldest no")
else:
    if b>c:
       print("b is the eldest no")
    else:
       if c>a:
          print("c is the greatest no")
          
indian=["roti","rice","daal"]
chinese=["friedrice","chowmein","noodles","manchurian"]
italian=["rosetto","pizza"]

if italian[1]=="pizza":
    italian[1]="burger"
    print(italian)

dish=input("What would you like to eat ?:")

if dish in indian:
    print("Yes, it is indian dish")
elif dish in chinese:
    print("Yes , it is chinese dish")
elif dish in italian:
    print("Yes, it is italian")
else:
    print("Sorry, it is not available")
    
x,y,z=30,20,18
print(x)
print(y)
print(z)
if 20 in (x,y,z):
    print("yes 20 is in z")
else:
    print("not existing")
    
age=int(input("Enter your age :"))
if age <18 :
    print("You cannot drive")
elif age == 18:
    print("We will think and let you know")
else:
    print("You can drive")
    
tp1=("friedrice","chowmein","noodles","manchurian")
if "noodles" in tp1:
    print("Yes it is available")
else:
    print("Not available")
    
d1={"k1":10,"k2":20,"k3":30}
if d1["k3"]==30:
    d1["k3"]=d1["k3"]+100
    print(d1)
    
#Short hand Notation of if else
a=int(input("enter a :"))
b=int(input("enter b:"))

print("a is lesser than b") if a<b else print(" a is greater than b")

print("Welcome to \n\n python ", end="")
print("Good \t afternoon")

choice="yes"
while (choice =="yes"):
    num1= int(input("Enter first Number :"))
    num2 = int(input("Enter Second Number :"))
    print("choose operation from below :")
    print("press + for addition")
    print("press - for subtraction")
    print("press * for multiplication")
    print("press / for division")
    operator= input("Enter your operator:") #+ - * /
    if num1==45 and num2==3 and operator=='*':
        print("555")
    elif num1==56 and num2==9 and operator=='+':
        print("77")
    elif num1==56 and num2==6 and operator=='/':
        print("4")
        
    elif operator=='+':
        print("Addition is =",num1+num2)
    elif operator=='-':
        print("Subtraction is=",num1-num2)
    elif operator=='*':
        print("Product is=",num1*num2)
    elif operator=='/':
        print("Division is=",num1/num2)
    else:
        print("Invalid opertor")  
    #print("Do you wish to continue ?")
    choice=input("Do you wish to continue ?") #yes or no

print("Thank You, Visit Again!!")

list1=[45,3]
list2=[56,9]
list3=[56,6]
num1= int(input("Enter first Number :"))
num2 = int(input("Enter Second Number :"))
print("choose operation from below :")
print("press + for addition")
print("press - for subtraction")
print("press * for multiplication")
print("press / for division")
operator= input("Enter your operator:") #+ - * /
if operator=="*":
    if num1 and num2 in list1:
        print("result:555")
    else:
        print("result:",num1*num2)
elif operator=="-":
    print("result:",num1-num2)
elif operator=="+":
    if num1 and num2 in list2:
        print("result:77")
    else:
        print("result:",num1+num2)
elif operator=="/":
    if num1 and num2 in list3:
        print("result:4")
    else:
        print("result:",num1/num2)
else:
    print("operation is not available")

#Guessing Game
secretno=10
no_of_guess=1
print("Number of guesses is limited to only 5 times:")  
while(no_of_guess <= 5):
    number=int(input("Guess the Number :"))
    if number < secretno:
        print("you enter less number ,please input greater number.\n")
    elif number >secretno:
        print("you enter greater number ,please input smaller number.\n")
    else:
        print("You Won !!\n")
        print(no_of_guess," no. of guesses you took to finish.")
        break
    print(5 - no_of_guess," no.of guesses left.")
    no_of_guess = no_of_guess+1
    if no_of_guess > 5:
        print("GAME OVER")
 '''
grocerylist=["Paneer","Cheese","Mango","Banana","Palak","Juice","Fruits"]

for i in grocerylist:
    print(i)

expenselist=[2340,2500,2100,3100,2900,3400,2700,1500]
sum=0
for e in expenselist:
    #print(expenselist)
    print(e)
    sum = sum + e
print("Total expense =",sum)

size= len(expenselist)
print(size)

#Print month number and expense and then print total expense
total=0
for i in range(0,len(expenselist)):
    #print(expenselist[i])
    print("Month :",i," Expense :",expenselist[i])
    total = total + expenselist[i]
print("Total expense =",total)

     


  
    





    
        
    

    
    



















        









