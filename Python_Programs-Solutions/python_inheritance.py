# #base class creation
# class Vehicle:
#     def __init__(self,mileage,cost):
#         self.mileage=mileage
#         self.cost=cost
#     
#     def show_details(self):
#         print("I am a vehicle")
#         print("Mileage of vehicle is",self.mileage)
#         print("Cost of vehicle is:",self.cost)
# #end of class vehicle
#         
# #Child class creation
# class Car(Vehicle):
#     def show_car_details(self):
#         print("I am a Car")
# 
# class Bike(Vehicle):
#     pass
#         
# c=Car(200,4500000) #instatntiation of child class object 'c'
# c.show_details()
# c.show_car_details()
# 
# b=Bike(250,56000)
# b.show_details()

#instantiating object of vehicle class
# v=Vehicle(500,3000000)
# v.show_details()

#Multiple Inheritance
#Base class-1
class Parent1:
    def set_string_one(self,string1):
        self.string1=string1
        
    def show_string_one(self):
        print("This is String1 of first base class")

#Base Class-2
class Parent2:
    def set_string_two(self,string2):
        self.string2=string2
        
    def show_string_two(self):
        print("This is string2 of second base class")

#Child class
class Child(Parent1,Parent2):
    def set_string_three(self,string3):
        self.string3=string3
        
    def show_string_three(self):
        print("This is string3 of the child class")
        
c1=Child()
c1.set_string_one("Iam string1 of Parent1")
c1.set_string_two("I am string2 of Parent2")

c1.set_string_three("I am string3 of child class")

c1.show_string_one()
c1.show_string_two()
c1.show_string_three()
