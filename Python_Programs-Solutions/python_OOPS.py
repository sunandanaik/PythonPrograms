#Creating a class
class Phone:
#     def set_color(self,color): #adding parameters(color, cost)
#               self.color=color
# 
#     def set_cost(self,cost):
#             self.cost=cost
            
    def __init__(self,color,cost,battery_life,memory_size):  #constructor in python
        self.color=color
        self.cost=cost
        self.battery_life=battery_life
        self.memory_size=memory_size

    def show_color(self):
            return self.color

    def show_cost(self):
            return self.cost

    def make_call(self):
        print("Making calls")
    def play_game(self):
        print("Playing the game")

#instantiate object for class Phone
#p1=Phone("Black",10000)
# p1.set_color("black") #invoking function
# p1.set_cost(10000)
p2=Phone("Gold",30000,"12mph",16)

print("Color of kaavya's phone is:",p2.show_color())
print("Cost of her phone is:",p2.show_cost())
p2.make_call()
p2.play_game()



# print("Color of my phone is:",p1.show_color())
# print("Cost of my phone is:",p1.show_cost())

# p1.play_game() #invoking of the functions
# p1.make_call()

