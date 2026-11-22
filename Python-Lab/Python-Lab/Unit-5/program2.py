# Program 2: Library management using a class

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(title)
        print(f"'{title}' added successfully")

    def remove_book(self, title):
        if title in self.books:
            self.books.remove(title)
            print(f"'{title}' removed")
        else:
            print(f"'{title}' not found")

    def display_books(self):
        print("\nAvailable Books:")
        for i, title in enumerate(self.books, start=1):
            print(f"{i}. {title}")


library = Library()
library.add_book("Python Programming")
library.add_book("Machine Learning Basics")
library.add_book("Data Structures")
library.remove_book("Data Structures")
library.display_books()
