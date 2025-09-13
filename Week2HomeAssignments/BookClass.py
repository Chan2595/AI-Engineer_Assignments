import datetime

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def get_age(self):
        """Return the age of the book in years"""
        current_year = datetime.datetime.now().year
        return current_year - self.publication_year


if __name__ == "__main__":
    # Create Book objects
    book1 = Book("Python Basics", "John Doe", 2015)
    book2 = Book("Artificial Intelligence", "Jane Smith", 2020)

    # Display details with age
    print(f"Title: {book1.title}, Author: {book1.author}, Age: {book1.get_age()} years")
    print(f"Title: {book2.title}, Author: {book2.author}, Age: {book2.get_age()} years")