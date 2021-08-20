# Create a library class
# display book
# lend book -(who owns the book if not present)
# add book
# return book
# Sunlibrary=library(listofbooks,library_name)
# dictionary(books-name of person)
# create main function and run infinite while loop asking users for their input.
class Library:
    def __init__(self,list,name):
        self.booksList=list
        self.name=name
        self.lendDict={}

    def displayBooks(self):
        print(f"We have following books in our Library:{self.name}")
        for book in self.booksList:
            print(book)

    def lendBooks(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user}) #updating dictionary
            print("Lender-Book database has been updated. You can take the book now.")
        else:
            print(f"Book is already being used by {self.lendDict[book]}")

    def addBooks(self,book):
        self.booksList.append(book)
        print("Book has been added to the book list.")

    def returnBooks(self,book):
        self.lendDict.pop(book)

if __name__ == '__main__':
    l=Library(['Python','Rich Daddy Poor Daddy','C++','Java','DSA'],"CodeWithSun")
    while(True):
        print(f"Welcome to the {l.name} Library. Enter your choice to continue .")
        print("1.Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option:")
            continue
        else:
            user_choice=int(user_choice)
        if user_choice == 1:
            l.displayBooks()
        elif user_choice==2:
            book=input("Enter the name of the book you want to lend:")
            user=input("Enter your name:")
            l.lendBooks(user,book)
        elif user_choice==3:
            book=input("Enter the name of the book you want to add:")
            l.addBooks(book)
        elif user_choice==4:
            book = input("Enter the name of the book you want to return:")
            l.returnBooks(book)
        else:
            print("Not a Valid option!!")

        print("Press Q to Quit and C to Continue :")
        choice=""
        while(choice!="q" and choice!="c"):
            choice=input()
            if choice=="q":
                exit()
            if choice=="c":
                continue
