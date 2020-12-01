#Multilevel Inheritance
#Base/Super class
class Parent:
    def get_name(self,name):
        self.name=name
        
    def show_name(self):
        return self.name
    
#end of super class
#derived class-1
class Child(Parent):
    def get_age(self,age):
        self.age=age
        
    def show_age(self):
        return self.age
     

#derived class-2
class GrandChild(Child):
    def get_gender(self,gender):
        self.gender=gender
    
    def show_gender(self):
        return self.gender
    
#instantiate the object of GrandChild class
g=GrandChild()

g.get_name("Krishna")
g.get_age(3)
g.get_gender("Male")

print("Name is:",g.show_name())
print("Age is:",g.show_age())
print("Gender is:",g.show_gender())

c=Child()
c.get_name("Kaushik")
print("Name of the child is:",c.show_name())