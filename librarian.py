from user import User

class Librarian(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)

    def borrow(self):
        print("Librarian does not borrow books.")

    def return_book(self):
        print("Librarian does not return books.")

    def show_menu(self):
        print("\n----- Librarian Menu -----")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. View All Books")
        print("5. Display Available Books")
        print("6. Display Borrowed Books")
        print("7. Exit")

    def add_book(self, books, book):
        books.append(book)
        print("Book added successfully.")

    def remove_book(self, books, book_id):
        for book in books:
            if book.book_id == book_id:
                books.remove(book)
                print("Book removed successfully.")
                return
        print("Book not found.")

    def search_book(self, books, title):
        for book in books:
            if book.title.lower() == title.lower():
                book.display_info()
                return
        print("Book not found.")

    def view_all_books(self, books):
        if not books:
            print("No books in the library.")
        else:
            for book in books:
                print("-" * 30)
                book.display_info()

    def display_available_books(self, books):
        print("\nAvailable Books:")
        for book in books:
            if book.available_copies > 0:
                book.display_info()

    def display_borrowed_books(self, books):
        print("\nBorrowed Books:")
        found_borrowed = False
        for book in books:
           
            if book.available_copies == 0:
                book.display_info()
                found_borrowed = True
        
        if not found_borrowed:
            print("No borrowed books currently.")