class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def get_category(self):
        if self.price >= 500:
            return "Premium"
        else:
            return "Standard"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("\n--- Library Books ---")

        for book in self.books:
            print("Book ID  :", book.book_id)
            print("Title    :", book.title)
            print("Author   :", book.author)
            print("Price    :", book.price)
            print("Category :", book.get_category())
            print("---------------------")


# Creating Library
library = Library()

# Adding books
library.add_book(Book(101, "Python Programming", "John Smith", 650))
library.add_book(Book(102, "Data Structures", "Robert Brown", 450))
library.add_book(Book(103, "Machine Learning", "David Lee", 800))

# Displaying all books
library.display_books()

"""
--- Library Books ---
Book ID  : 101
Title    : Python Programming
Author   : John Smith
Price    : 650
Category : Premium
---------------------
Book ID  : 102
Title    : Data Structures
Author   : Robert Brown
Price    : 450
Category : Standard
---------------------
Book ID  : 103
Title    : Machine Learning
Author   : David Lee
Price    : 800
Category : Premium
---------------------
"""




