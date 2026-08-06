from user import User

class Student(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.borrowed_books = []

    def borrow(self, book):
        if len(self.borrowed_books) < 3:
            if book.available_copies > 0:
                book.borrow_book()
                self.borrowed_books.append(book)
                print("Book borrowed successfully.")
            else:
                print("Book is unavailable.")
        else:
            print("Student cannot borrow more than 3 books.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print("Book returned successfully.")
        else:
            print("This book was not borrowed.")

    def show_menu(self):
        print("\n----- Student Menu -----")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. Exit")