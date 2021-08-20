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

   def __repr__(self):
     return f'{self.title} by {self.author}, price {self.get_price()}'

#Child class-1	 
class Poetry(Book):
   def __init__(self, title, poems_count, author, price):
     super().__init__(title, author, price)
     self.poems_count = poems_count

#child class-2
class Play(Book):
   def __init__(self, title, genre, author, price):
     super().__init__(title, author, price)
     self.genre = genre

   def __repr__(self):
     return f'{self.genre} Play: {self.title} by {self.author}, price {self.get_price()}'

#child class-3
class Novel(Book):
   def __init__(self, title, pages, author, price):
     super().__init__(title, author, price)
     self.pages = pages 
	 
#Objects instantiated of all classes
poem_2 = Poetry('Milk and Honey', 179, 'Rupi Kaur', 320)
play_2 = Play('An Ideal Husband', 'Comedy', 'Oscar Wilde', 240)
novel_2 = Novel('The Alchemist', 161, 'Paulo Coelho', 180)
 
print(poem_2)
print(play_2)
print(novel_2)