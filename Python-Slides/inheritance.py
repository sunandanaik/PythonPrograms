class Book():
   def __init__(self, title, author, price):
     self.title = title
     self.author = author
     self.__price = price
     self.__discount = None

   def set_discount(self, value):
     self.__discount = value

   def get_price(self):
     if self.__discount is None:
       return self.__price
     else:
       return self.__price * (1 - self.__discount) 
	   
#Child Class-1
class Poetry(Book):
   def __init__(self, title, poems_count, author, price):
     super().__init__(title, author, price)
     self.poems_count = poems_count

   def __repr__(self):
     return f'Poetry: {self.title} by {self.author}, price {self.get_price()}'

#Child class-2
class Play(Book):
   def __init__(self, title, genre, author, price):
     super().__init__(title, author, price)
     self.genre = genre

   def __repr__(self):
     return f'{self.genre} Play: {self.title} by {self.author}, price {self.get_price()}'

#Child class-3
 class Novel(Book):
   def __init__(self, title, pages, author, price):
     super().__init__(title, author, price)
     self.pages = pages

   def __repr__(self):
     return f'Novel: {self.title} by {self.author}, price {self.get_price()}' 



#Instantiate Poetry class object	 
poem_1 = Poetry('Leaves of Grass', 383, 'Walt Whitman', 600)
print(poem_1)
poem_1.set_discount(0.15)
print(poem_1) 

play_1 = Play('Romeo and Juliet', 'Tragedy', 'William Shakespeare', 160)
novel_1 = Novel('To kill a Mockingbird', 281, 'Harper Lee', 310)
print(play_1)
print(novel_1)