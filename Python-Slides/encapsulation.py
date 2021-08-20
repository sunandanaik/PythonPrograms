'''Encapsulation is the process of making certain attributes inaccessible to their clients and can only be accessed through certain methods. 
The inaccessible attributes are called private attributes, and the process of making certain attributes private is called information hiding. 
Private attributes begin with two underscores.Private attributes are accessed through methods called getter and setter. '''

class Poetry():
   def __init__(self, title, poems_count, author, price):
     self.title = title
     self.poems_count = poems_count
     self.author = author
     self.__price = price
     self.__discount = 0.20 #private attribute declared
	 
   def set_discount(self, value):
     self.__discount = value

   def get_price(self):
     if self.__discount is None:
       return self.__price
     else:
       return self.__price * (1 - self.__discount)
	   
   def __repr__(self):
     return f'Poetry: {self.title} by {self.author}, price {self.price}'
 
 #Object instantiated
 poem_1 = Poetry('Leaves of Grass', 383, 'Walt Whitman', 600)
 
 retail_purchase = Poetry('Leaves of Grass', 383, 'Walt Whitman', 600)
 bulk_purchase = Poetry('Leaves of Grass', 383, 'Walt Whitman', 600)
 
 # assign 30% discount to bulk purchase alone
 bulk_purchase.set_discount(0.30)
 
 print(retail_purchase.get_price())
 print(bulk_purchase.get_price())
 print(retail_purchase)
 print(bulk_purchase)
 
 #printing the object
 print(poem_1.author)
 print(poem_1.title)
 print(poem_1.price)
 print(poem_1.__discount) 