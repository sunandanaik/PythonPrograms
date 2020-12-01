"""This function greets to the person passed in as
a parameter"""
#Example-1
#Function definition  -2
def greet(name):
    print("Hello, " + name + ". Good morning!")
    
#function calling-1
greet("Kaavya")

#Example-2
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num  #print(num)
    else:
        return -num  # -num= -(-4)=4


print(absolute_value(2))

print(absolute_value(-4))


#Example-3
def my_func():
    x = 10
    print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)

#Example-4
def hello_func(name,msg):  #function definition with multiple parameters
    print("Hi", name + ","+" "+msg)

name="Jhonny"
msg="How are you?"
# name=input("Enter the Name:")
# msg=input("Enter your message:")

hello_func(name,msg) #function calling here

#Example-5
def greeting(name, msg="Good morning!"):  #default value to the parameter passed is it clear
   
    print("Hello", name + ', ' + msg)


greeting("Kate") #one time function is calling
greeting("Bruce", "How do you do?")  #sec time function is called
greeting(msg = "How do you do?",name = "Bruce") #third time function calling using keyword arguments(positional arguments)
greeting("Bruce","How do you do?")

#Example-6

def addnum(n1,n2,n3):
    sum=n1+n2+n3
    return sum
    #print("Sum of three nos is:"+sum)
    
def average_num(result):
    avg=result/3
    print("\nAverage:",avg)
    
result=addnum(10,20,30)
print("\nSum of three nos is:",result)
average_num(result)

#Example-7
def greet(*names):   #function definition using arbitary argument
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John","Kaavya","Kaushik") #function calling

#Factorial of a number using recursive function
def factorial(x):  #function definition x=1
     if x == 1:     #1==1 yes
        return 1
     else:
        return (x * factorial(x-1))  #3*factorial(2) #3*2*factorial(1)


num = 3  #3!=3*2*1=6
print("The factorial of", num, "is", factorial(num))  #function calling passing a parameter(3)  =3*2*1=6

#Print "Hello World" 10 times
def PrintMessage():
    for x in range(1,11):
        print("Hello World")

print("Greet message is coming:")
PrintMessage()
print("How are you?")
print("Life is good")
PrintMessage() #calling of function any no of times done

def PrintMessage(message): #function defined with argument/parameter
    for x in range(1,11):
        print(message)

print("Greet message is coming:")
message="Hello World"
PrintMessage(message)
print("How are you?")
print("Life is good")
PrintMessage("I love Python") #calling of function any no of times done


def PrintMessage(message,no_of_times): #function defined with multiple arguments/parameters
    for x in range(1,no_of_times+1):
        print(message)

print("Greet message is coming:")
message="Hello World"
PrintMessage(message,10)
print("How are you?")
print("Life is good")
PrintMessage("I love Python",5) #calling of function any no of times done


def PrintMessage(message="I am coding",no_of_times=10): #function defined with defaultvalue to arguments/parameters
    for x in range(1,no_of_times+1):
        print(message)

print("Greet message is coming:")
message="Hello World"
PrintMessage(message)
print("How are you?")
print("Life is good")
PrintMessage("I love Python",5) #calling of function any no of times done
PrintMessage() #calling function without passing parameter values then default value will be assigned.


def PrintIntegers(*values):  #* means any no of values(arbitary argument)
    print(values)
    for x in values:
        print(x)
        
PrintIntegers(3,4,6,10,12) #calling function using any no of values to the parameter


def printvalues(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)
    
printvalues(10,20,30) #orderly values will be given to the respective arguments
printvalues(c="10",b="20",a="30") #this is unordered


def add(a,b,c):
    return a+b+c

sum=add(10,5,7)
print("Sum is:",sum)
#or
print(add(2,3,4))

#New Program -to print list in sorted order
def InputNumber(ilist):
    while True:
         number=int(input("Enter Next Number:"))
         if number !=0:
           ilist.append(number)
        #PrintSortedList(ilist)
         else:
            print("program ended")
            break
    
def PrintSortedList(ilist):
    ilist.sort()
    for l in ilist:
        print(l)
    
ilist=[]
InputNumber(ilist)
PrintSortedList(ilist)

#Calculator Program Using function
def inputnumber():
    return int(input("Enter Next Number:"))

def AskOperation():
    return(int(input("Add-1,Sub-2,Multi-3,Div-4\n")))
    

def Add(a,b):
    return a+b
def Sub(a,b):
    return a-b
def Multi(a,b):
    return a*b
def Div(a,b):
    return a/b

opt=AskOperation()

if opt==1:
    print(Add(inputnumber(),inputnumber()))
elif opt==2:
    print(Sub(inputnumber(),inputnumber()))
elif opt==3:
    print(Multi(inputnumber(),inputnumber()))
elif opt==4:
    print(Div(inputnumber(),inputnumber()))

#Example
def sun():
    pass
sun()

#return statement
def abc():
    print("How are you?")

abc()

#use docstring in triple quotes
def add2(a,b):
    """
    This function helps us to add two values of same data type.
    a:give same datatype values for a and b.
    b:give same datatype values for a and b.
    """
    return a+b

print(add2(345,45))

#arbitary args
def super_add(*args):
    print(type(args))
    add=0
    for i in args:
        add+=i
    return add

print("Total =",super_add(2,2,3))

#default args
def no_args(a=10,b=20):
    return a+b

print("Ans:",no_args()) #calling function without args values
print("Ans:",no_args(a=40,b=100)) # or calling function with args values

def interest(a,b,c=30,d=40):
    return a+b+c+d+e

print(interest(20,10))

#ex- kwargs
d={"keys":"values"}
def wow(**kwargs):
    print(type(kwargs))
    return kwargs

print(wow(a=10,b=20))

#ex
def new_len(s):
    """
    This is personal length function
    s:any iterable value
    """
    length=0
    for i in s:
        length+=1
    return length

print("Length=",new_len("I live in Goa"))

#calculator program using function
def sum_prod(a,b):
    choice=input("Enter your choice:")
    if choice=="Sum":
        return a+b
    elif choice=="prod":
        return a*b
    else:
        return "Valid choice"
print("Result:",sum_prod(2,3))










