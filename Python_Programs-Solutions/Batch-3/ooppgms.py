# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 17:34:35 2021

@author: DELL


def test(a,b):
    num1=a
    num2=b
    sum=num1+num2
    print(sum)
    
test(10,20)


#Step-1:creating class "Pokemon"
class Pokemon():
    name=""
    Type=""
    health=""
    #special method-initialize
    def __init__(self,name,Type,health):
        self.name=name
        self.Type=Type
        self.health=health
    
    def attack(self):
        print("Electric attack!!.Zhoop!!!")
        
    def dodge(self):
        print("Pikachu Dodge!")

    def evolve(self):
        print("Evolving to Raichu!!!!")
#end of class  
     
#Step-2:Creating object of "Pokemon" class
object1= Pokemon("Pikachu","Electric",70)#init() is called 
print(object1.name)
print(object1.Type)
print(object1.health)
object1.attack()
object1.dodge()
object1.evolve()


def addition(a,b):
    sum=a+b
    print("Addition is:",sum)
    
def subtraction(a,b):
    sub=a-b
    print("Difference is:",sub)
    
def product(a,b):
    prod=a*b
    print("Product is :",prod)

a=10
b=20    
addition(a,b)
product(a,b)
subtraction(a,b)


class Calculator():
    a=0
    b=0
    #Setter method
    def setA(self,a):
        self.a=a
        
    def setB(self,b):
        self.b=b
        
        
    def addition(self):
        sum=self.a+self.b
        print("Addition is:",sum)
    
    def subtraction(self):
        sub=self.a-self.b
        print("Difference is:",sub)
    
    def product(self):
        prod=self.a*self.b
        print("Product is :",prod)
        
#end of class
basic=Calculator()
basic.setA(10)
basic.setB(20)


basic.addition()
basic.subtraction()
basic.product()

sci=Calculator()

class Calculator():
    a=0
    b=0
    
    #Special Method(Constructor Method)
    def __init__(self,a,b):
        self.a=a
        self.b=b
        print("Constructor called")
        
    def addition(self):
        sum=self.a+self.b
        print("Addition is:",sum)
    
    def subtraction(self):
        sub=self.a-self.b
        print("Difference is:",sub)
    
    def product(self):
        prod=self.a*self.b
        print("Product is :",prod)
    
basic=Calculator(20,50)
basic.addition()
basic.product()
basic.subtraction()
print("Class Over")

#Check the even and odd numbers from the given list[1,2,3,4,5,6,...10]
numlist=[1,2,3,4,5,6,7,8,9,10]
for i in numlist:
    if i % 2 ==0:
        print("Even No:",i)
    else:
        print("Odd No:\t",i)



def check_even(numlist):
    print("List of Even Nos:")
    for i in numlist:
        if i%2==0:
            print(i,end=" ")

numlist=[1,2,3,4,5,6,7,8,9,10]            
check_even(numlist)

def check_odd(numlist):
    print("\nList of Odd Nos:")
    for i in numlist:
        if i%2!=0:
            print(i,end=" ")

numlist=[1,2,3,4,5,6,7,8,9,10]            
check_odd(numlist)
    

class Numbers():
    
    def check_even(self,numlist):
        print("\nList of Even Nos:")
        for i in numlist:
            if i%2==0:
                print(i,end=" ")
                
    def check_odd(self,numlist):
        print("\nList of Odd Nos:")
        for i in numlist:
            if i%2!=0:
                print(i,end=" ")
    
n1=Numbers()
numlist=[1,2,3,4,5,6,7,8,9,10] 
n1.check_even(numlist)
n1.check_odd(numlist)


class Human():
    def __init__(self,name,occupation):
        self.name=name
        self.occupation=occupation
        
    def do_work(self):
        if self.occupation == "Actor":
            print("I shoot movies")
        elif self.occupation == "Tennis Player":
            print("I play tennis")
        elif self.occupation == "PM":
            print("I serve the Nation India")
    
    def speaks(self):
        print("Hello Everyone, I am ",self.name)
    

tom=Human("Tom Cruise","Actor")
tom.speaks()
tom.do_work()


maria=Human("Maria Sharapova","Tennis Player")
maria.speaks()
maria.do_work()
   

modi=Human("Narendra Modi","PM")
modi.speaks()  
modi.do_work() 
"""

class Phone():
    def __init__(self,color,cost,brand,size):
        self.color=color
        self.cost=cost
        self.brand=brand
        self.size=size
        
    def makes_call(self):
        print(self.brand,"making call")
    
    def play_games(self):
        if self.brand =="Samsung Galaxy":
            print("Moderate gaming Experience")
        elif self.brand=="Redmi Pro":
            print("You wont be having Gaming Experience")
    
samsung=Phone("Silver",10000,"Samsung Galaxy","128GB")
samsung.makes_call()
samsung.play_games()

redmi=Phone("Black",5000,"Redmi Pro","32GB")
redmi.makes_call()
redmi.play_games()

print(redmi.__class__.__name__)

def addition(a,b):
    pass

print(addition.__name__)





   
        