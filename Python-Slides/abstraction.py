from abc import ABC, abstractmethod

 class Book(ABC):
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

   @abstractmethod
   def __repr__(self):
     return f'{self.title} by {self.author}, price {self.get_price()}'

 class Poetry(Book):
   def __init__(self, title, poems_count, author, price):
     super().__init__(title, author, price)
     self.poems_count = poems_count

   def __repr__(self):
     return f'Poetry: {self.title} by {self.author}, {self.poems_count} poems, price {self.get_price()}'

 class Play(Book):
   def __init__(self, title, genre, author, price):
     super().__init__(title, author, price)
     self.genre = genre

   def __repr__(self):
     return f'Play: {self.title} by {self.author}, {self.genre} genre, price {self.get_price()}'

 class Novel(Book):
   def __init__(self, title, pages, author, price):
     super().__init__(title, author, price)
     self.pages = pages

   def __repr__(self):
     return f'Novel: {self.title} by {self.author}, {self.pages} pages, price {self.get_price()}' 
	 
#Object Instantiation
poem_3 = Poetry('Life on Mars', 33, 'Tracy K. Smith', 100)
play_3 = Play('Death of a Salesman', 'Tragedy', 'Arthur Miller', 240)
novel_3 = Novel('Peril at End House', 270, 'Agatha Christie', 210)
 
print(poem_3)
print(play_3)
print(novel_3) 