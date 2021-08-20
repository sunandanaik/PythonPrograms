import math

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divisible(a,b):
    return a/b

def exp(a):
    return a**2

def sqrt(s):
    return math.sqrt(s)

def sin(x):
    result=math.sin(x)
    return result

def cos(x):
    result=math.cos(x)
    return result

def tan(x):
    result=math.tan(x)
    return result

#Choosing the operation
print("""
Choose a number for the following operations
1-Addition
2-Subtraction
3-Multiplication
4-Division
5-Exponent
6-Square Root
7-sin
8-cos
9-tan
""")
op=int(input("What operation do you want to perform?:"))

#calculator script
while op<10:
    if op == 1:
        print("Enter the parameters:")
        x1=int(input("Enter x:"))
        y1=int(input("Enter y:"))
        res1=add(x1,y1)
        print("Addition :",res1)
    elif op == 2:
        print("Enter the parameters:")
        x2=int(input("Enter x:"))
        y2=int(input("Enter y:"))
        res2=subtract(x2,y2)
        print("Subtraction :",res2)
    elif op == 3:
        print("Enter the parameters:")
        x3=int(input("Enter x:"))
        y3=int(input("Enter y:"))
        res3=multiply(x3,y3)
        print("Multiplication :",res3)   
    elif op == 4:
        print("Enter the parameters:")
        x4=int(input("Enter x:"))
        y4=int(input("Enter y:"))
        res4=divisible(x4,y4)
        print("Division :",res4)
    elif op == 5:
        print("Enter the parameters:")
        x5=int(input("Enter x:"))
        
        res5=exp(x5)
        print("Square :",res5)
    elif op == 6:
        print("Enter the parameters:")
        x6=int(input("Enter x:"))
        
        res6=sqrt(x6)
        print("Square Root :",res6)
    elif op == 7:
        print("Enter the parameters:")
        x7=int(input("Enter x:"))
        
        res7=sin(x7)
        print("sin :",res7)
    elif op == 8:
        print("Enter the parameters:")
        x8=int(input("Enter x:"))
        
        res8=cos(x8)
        print("cos :",res8)
    elif op == 9:
        print("Enter the parameters:")
        x9=int(input("Enter x:"))
        
        res9=tan(x9)
        print("tan :",res9)
        
    else:
        print('Choose another operation:')
        
    new_num=int(input("Do you want to continue-(yes -1), (No-0):"))
    if new_num==1:
        op=int(input("Enter operation:"))
    elif new_num==0:
        print("Thanks for using the Scientific calculator!!")
        break
        