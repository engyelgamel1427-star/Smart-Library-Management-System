class Book:
    def __init__(self, book_id, title, author, category, available_copies):
        self.book_id = int(book_id)
        self.title = title
        self.author = author
        self.category = category
        self.available_copies = int(available_copies)

    def display_info(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Category: {self.category}")
        print(f"Available Copies: {self.available_copies}")

    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("Book borrowed successfully.")
        else:
            print("Sorry, this book is unavailable.")

    def return_book(self):
        self.available_copies += 1
        print("Book returned successfully.")

    def to_file_string(self):
        return f"{self.book_id},{self.title},{self.author},{self.category},{self.available_copies}\n"

def load_books_from_file(filename="books.txt"):
    books = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    book_id, title, author, category, copies = parts
                    books.append(Book(book_id, title, author, category, copies))
    except FileNotFoundError:
        default_books = [
            Book(1, "Python Basics", "Ahmed Ali", "Programming", 3),
            Book(2, "Data Structures", "Sara Mohamed", "Computer Science", 2),
            Book(3, "Machine Learning", "John Smith", "AI", 1)
        ]
        save_books_to_file(default_books, filename)
        return default_books
    return books

def save_books_to_file(books, filename="books.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for book in books:
            file.write(book.to_file_string())