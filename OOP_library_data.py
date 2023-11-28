# -*- coding: utf-8 -*-
"""Day2_OOP_CindhaRizkiana.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hF5JrotjoC-ErOJMO5lI20SQklo7_Es0
"""

import datetime

class book:
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies
        self.due_date = None

    def checkout_book(self):
        if self.available_copies > 0:
           self.available_copies -= 1
           self.set_due_date()
           return True
        else:
            return "No available copies of this book."

    def return_book(self):
        self.available_copies += 1
        self.due_date = None

    def set_due_date(self):
          self.due_date = datetime.date.today() + datetime.timedelta(days=7)

class user:
    def __init__(self, name, library_id):
        self.name = name
        self.library_id = library_id
        self.check_the_books = []

    def checkout_book(self, book):
        if book.checkout_book():
          self.check_the_books.append(book)

    def return_book(self, book):
        for check_the_books in self.check_the_books:
            if check_the_books == book:
                self.check_the_books.remove(book)
                check_the_books.return_book()
                break

    def display_checked_out_books(self):
        print(f"Books checked out by {self.name} (ID: {self.library_id}):")
        for book in self.check_the_books:
            print(f"{book.title} by {book.author}")

    def check_due_date(self,book):
        if book in self.check_the_books:
            return book.due_date
        return None


class library:
    def __init__(self):
        self.book_collection = []

    def add_book(self, book):
        self.book_collection.append(book)

    def display_available_books(self,book):
        print("Available books in the library:")
        for book in self.book_collection:
            print(f"{book.title} by {book.author} - Available Copies: {book.available_copies}")

    def search_books(self, author):
        print(f"Books by {author} in the library:")
        for book in self.book_collection:
            if book.author == author:
                print(f"{book.title} - Available Copies: {book.available_copies}")


if __name__ == "__main__":

    inside_library = library()

# Add book to the library
    print(f"Add books to the library: ")
    book1 = book("Harry Potter", "J.K. Rowling", 5)
    inside_library.add_book(book1)
    print(f"{book1.title} added to the library")

    book2 = book("The God of Small Things", "Arundhati Roy", 4)
    inside_library.add_book(book2)
    print(f"{book2.title} added to the library")

    book3 = book("Pride and Prejudice", "Jane Austen", 3)
    inside_library.add_book(book3)
    print(f"{book3.title} added to the library")

# Create user accounts with unique library IDs
    user1 = user("Bobby", "TW001")
    user2 = user("Danny", "TW002")
    user3 = user("Anne", "TW003")

# Check out and return books
    print(f"Lists of check out and return the book")
    user1.checkout_book(book1)
    user2.checkout_book(book2)
    user3.checkout_book(book3)

# Check the due date
    due_date = user1.check_due_date(book1)
    if user1.checkout_book(book1):
     print(f"Due date for {book1.title}: {due_date}")

    # user1.display_checked_out_books()
    # user2.display_checked_out_books()
    # user3.display_checked_out_books()

# Display available books and search for books by author
    inside_library.display_available_books(book)

# Search for books by author
    author_to_search = "J.K. Rowling"
    inside_library.search_books(author_to_search)
    author_to_search = "Jane Austen"
    inside_library.search_books(author_to_search)

