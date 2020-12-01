class Computer:

    def __init__(self):
        self.__maxprice = 900   #__maxprice is private variable

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000 #not possible bcoz maxprice is private variable
c.sell()

# using setter function
c.setMaxPrice(1000) #here u can access private variable using setter method
c.sell()

a=10
b=20
print(a+b)
print("Hello" +"Kaavya")
