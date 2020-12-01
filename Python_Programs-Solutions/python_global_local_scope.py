#Ex-1
x = "Goa"  #global variable

def foo():  # function definition here done
    print("x inside function:", x)


foo() #function calling here done
print("x outside function:", x)

#ex-2
y=20 #global variable

def foo1():
    #print(y)
    
    global y
    y = y * 2
    print(y)

foo1()

#Ex-3
def fun_local():
    z = "local" #local variable created
    print(z)
#end of function

fun_local()
#print(z) #not allowed bcoz no permission

#Ex-4
add=0 #3 global variables
n1=10
n2=20

def add_num():
    
    add=n1+n2 #add variable is local within the function
    return add
#end of function    
  
add=add_num()
print("Sum is:",add)

#Ex-5
#when global and local variables are having same name
a = 5  #global var

def foo():
    a = 10 #local var
    print("local a:", a)


foo()
print("global a:", a)

#Ex-6
#Nonlocal var
def outer():  #outer function definition here
    b = "bangalore" #local variable

    def inner(): #inner function definition here
        nonlocal b
        b = "goa" #nonlocal var
        print("inner:", b)

    inner()
    print("outer:", b)

outer()

#Local and global variable more practice

a=10
a=15
print(a)

#Ex-7
var1=10 #global scope

def sun():
    var1=15 #local scope
    var2=30
    print("This is inside the function var1 value:",var1,id(var1))
    
sun()
print("This is outside the function var1 value:",var1,id(var1))

#Ex-8
var3=10 #global scope

def hrutu():
    b=20 #local scope
    print(var3)
    
var3=hrutu()
#print(b) #will not work bcoz local scope cannot be accessed globally here
print(var3)

#Ex-9
a=10
def fun1():
    global a #using global keyword
    a=20
    print(a)

fun1()
print(a)



