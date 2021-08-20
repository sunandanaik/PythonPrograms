class Poetry():
   def __init__(self, title, poems_count, author, price):
     self.title = title
     self.poems_count = poems_count
     self.author = author
     self.price = price
   
   #to give details about the attributes, i.e., the title, author name, etc. 
   def __repr__(self):
     return f'Poetry: {self.title} by {self.author}, price {self.price}'
	 
# objects instantiation
poem_1 = Poetry('Leaves of Grass', 383, 'Walt Whitman', 600)
poem_2 = Poetry('Milk and Honey', 179, 'Rupi Kaur', 320)
poem_3 = Poetry('Life on Mars', 33, 'Tracy K. Smith', 100)

# printing the objects
print(poem_1)
print(poem_2)
print(poem_3) 