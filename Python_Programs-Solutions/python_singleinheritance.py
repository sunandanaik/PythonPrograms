# parent class
class Bird:
    
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        super().whoisThis()  #this invokes function of the super class(base class/parent class)
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin() #instantiate the object of child class
peggy.whoisThis()
peggy.swim()
peggy.run()


