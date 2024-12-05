#1  Input method


# class Book:
#     def __init__(self):
#         self.book = {};
#         self.bookname= input(f"Enter the bookname")
#         print(self.bookname)

#     def AddBookDetails(self):
#          self.book_name=input("Enter the BOOK NAME -")
#          self.author=input("Enter the author of the book -")
#          self.pages=input("Enter the number of pages")
#          self.book.update({
#              'Book':self.book_name,
#              'Author':self.author,
#              'Pages':self.pages
#          })
#          print(f'The book you entered has the following details{self.book}')


# p1=Book()
# p1.AddBookDetails()

#2  arguments method

class Book:
    def __init__(self):
        self.book = {};
        

    def AddBookDetails(self,book_name,author,pages):
         self.book.update({
             'Book':book_name,
             'Author':author,
             'Pages':pages
         })
         print(f'The book you entered has the following details{self.book}')


p1=Book()
p1.AddBookDetails('KiteRunner','KhaledHossaini',300)
p1.AddBookDetails('WhenTheMoonSplit','SafiUrRahman',500)
p1.AddBookDetails('PrideAndPrejudice','JaneAustin',300)

