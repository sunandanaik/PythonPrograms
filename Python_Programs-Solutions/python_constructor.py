class Employee:
    #creating constructor
    def __init__(self,name,age,gender,salary,no_of_expr,higher_edu):
        self.name=name
        self.age=age
        self.gender=gender
        self.salary=salary
        self.no_of_expr=no_of_expr
        self.higher_edu=higher_edu
        
    def show_employee_details(self):
        print("Name of employee is:", self.name)
        print("\nAge of employee is:", self.age)
        print("\nGender of employee is:",self.gender)
        print("\nSalary of employee is:", self.salary)
        print("\nNo of experience he has:",self.no_of_expr)
        print("\nHigher Education is:", self.higher_edu)

#instantiate object of employee class
emp=Employee("Jack",32,"Male",50000,15,"MTech")
emp.show_employee_details()