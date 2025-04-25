import pandas as pd
import matplotlib.pyplot as plt

class Book:
    def __init__(self, title, author, year, status='Available'):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def display_books(self):
        print("\nAll Books in Library:")
        for book in self.books:
            print(f"{book.title} by {book.author} ({book.year}) - {book.status}")
    
    def display_available_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            if book.status == 'Available':
                print(f"{book.title} by {book.author} ({book.year})")
    
    def to_dataframe(self):
        data = {'Title': [], 'Author': [], 'Year': [], 'Status': []}
        for book in self.books:
            data['Title'].append(book.title)
            data['Author'].append(book.author)
            data['Year'].append(book.year)
            data['Status'].append(book.status)
        return pd.DataFrame(data)
    
    def visualize_books_per_author(self):
        df = self.to_dataframe()
        author_counts = df['Author'].value_counts()
        author_counts.plot(kind='bar', color='skyblue', edgecolor='black')
        plt.xlabel('Author')
        plt.ylabel('Number of Books')
        plt.title('Number of Books per Author')
        plt.xticks(rotation=45)
        plt.show()

library = Library()
library.add_book(Book("Python Basics", "John Doe", 2020))
library.add_book(Book("Data Science", "Jane Smith", 2021, status='Checked Out'))
library.add_book(Book("Machine Learning", "John Doe", 2022))
library.add_book(Book("Deep Learning", "Alice Brown", 2019))

library.display_books()
library.display_available_books()
library.visualize_books_per_author()