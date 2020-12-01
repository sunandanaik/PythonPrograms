# Program to show the use of lambda functions
double = lambda x: x * 2+x  #here x is 2-- 2*2+2=6

print("Result is:",double(2))  #6


#or
def double(x):
    return(x * 2+x)

print("\nAnswer is:", double(2))

#ex 1
def xyx(a):
    return a**2  #3 **2=power(3,2)=9

print("Square of the number is:",xyx(3)) #function calling here done

#now using lambda function
l=lambda a : a**2
print("l is:",l(3))

#ex-2
def linear(x1,y1):
    return 2*(x1**2)+y1

print(linear(3,2))

#now using lambda func
linear1=lambda x1,y1 : 2*(x1**2)+y1
print(linear1(3,2))

#List Comprehension
mylist=[]  #empty list created
for i in range(1,6):
    mylist.append(i ** 2)
print(mylist)

#or
l1=[i ** 2 for i in range(1,6)]
print(l1)

#print even numbers
even=[]  #empty list created
for i in range(0,21,2):
    even.append(i)
print(even)

#now using list comprehension print even nos.
even1=[i for i in range(0,21,2)]
print(even1)

#print odd numbers into list using list comprehension method
odd1=[i for i in range(1,31,2)]
print("List of Odd numbers are:\n")
print(odd1)

#now using function
elist=[] #empty list created
def evennum():  #function definition
    for i in range(0,21,2):
        elist.append(i)
    print(elist)

evennum()  #function calling here done

olist=[]
def oddnum():
    for i in range(1,31,2):
        olist.append(i)
    print("Odd numbers in list are:")
    print(olist)
    
oddnum()

#Ex-list comprehension
nums=[1,2,3,4,5,6,7,8,9,10]
num2=[]
for i in nums:
    num2.append(i*2)
print(num2)

#now using list comprehension
num3=[i*2 for i in nums]
print(num3)

#Ex
responses=[["Bob","y"],
           ["Bill","n"],
           ["Fred","y"]
           ] #2d list
print(responses)
going=[i[0] for i in responses if i[1]=="y"]
print(going)
        
