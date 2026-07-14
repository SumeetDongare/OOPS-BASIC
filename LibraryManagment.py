class Books:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_available = True
    def display_book_info(self):
        print(f"Title:{self.title}\nAuthor:{self.author}")

class Student_ID:
    def __init__(self,student_id,name):
        self.student_id = student_id
        self.name = name
        self.borrowed_books = []
    def display_student_info(self):
        print(f"Student ID:{self.student_id}\nName:{self.name}")
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print(f"- {book.title} by {book.author}")

class Library:
    def __init__(self):
        self.books = []
        self.students = []
    
    #add book to library 
    def add_book(self,book):
        self.books.append(book)
        print("Book added successfully.")
    
    #add student to library
    def add_student(self,student):
        self.students.append(student)
        print("Student added successfully.")
    
    #remove book from library
    def remove_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print("Book removed successfully.")
        else:
            print("Book not found in library.")
    
    #remove student from library
    def remove_student(self,student):
        if student in self.students:
            self.students.remove(student)
            print("Student removed successfully.")
        else:
            print("Student not found in library.")
    
    #search book in library
    def search_book(self,title):
        for book in self.books:
            if book.title == title:
                return book
        print("Book not found in library.")
        return None
    
    #borrow book from library 
    def borrow_book(self,student,book):
        if book in self.books:
            if book.is_available:
                book.is_available = False
                student.borrowed_books.append(book)
                print("Book borrowed successfully.")
            else:
                print("Book is not available.")
        else:
            print("Book not found in library.")
    
    #return book to library
    def return_book(self,student,book):
        if book in student.borrowed_books:
            book.is_available = True
            student.borrowed_books.remove(book)
            print("Book returned successfully.")
        else:
            print("Book not borrowed by the student.")

# Creating Library Object
library = Library()

# Creating Book Objects
book1 = Books("Python Programming", "John Smith")
book2 = Books("Data Structures", "Mark Allen")
book3 = Books("Object Oriented Programming", "Robert Martin")


# Creating Student Objects
student1 = Student_ID(101, "Rahul")
student2 = Student_ID(102, "Amit")

# Adding Books to Library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Adding Students to Library
library.add_student(student1)
library.add_student(student2)


# Display Book Information
book1.display_book_info()

# Display Student Information
student1.display_student_info()

# Search Book
searched_book = library.search_book("Python Programming")

if searched_book:
    searched_book.display_book_info()


# Borrow Book
library.borrow_book(student1, book1)

# Display Student After Borrowing
student1.display_student_info()

# Try Borrowing Same Book Again
library.borrow_book(student2, book1)

# Return Book
library.return_book(student1, book1)

# Display Student After Returning
student1.display_student_info()

# Remove Book
library.remove_book(book3)

# Remove Student
library.remove_student(student2)   