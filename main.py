from book import Book, load_books_from_file, save_books_to_file
from student import Student
from teacher import Teacher
from librarian import Librarian

books = load_books_from_file()

student = Student(101, "Ali")
teacher = Teacher(201, "Mona")
librarian = Librarian(301, "Admin")

while True:
    print("\n===== Smart Library Management System =====")
    print("1. Librarian")
    print("2. Student")
    print("3. Teacher")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input.")
        continue

    if choice == 4:
        print("Thank you for using Smart Library Management System!")
        break

    elif choice == 1:
        librarian.show_menu()
        librarian_choice = int(input("Enter your choice: "))

        if librarian_choice == 1:
            book_id = int(input("Book ID: "))
            title = input("Title: ")
            author = input("Author: ")
            category = input("Category: ")
            copies = int(input("Available Copies: "))

            new_book = Book(book_id, title, author, category, copies)
            librarian.add_book(books, new_book)
            save_books_to_file(books)

        elif librarian_choice == 2:
            book_id = int(input("Enter Book ID to remove: "))
            librarian.remove_book(books, book_id)
            save_books_to_file(books)

        elif librarian_choice == 3:
            title = input("Enter Book Title: ")
            librarian.search_book(books, title)

        elif librarian_choice == 4:
            librarian.view_all_books(books)

        elif librarian_choice == 5:
            librarian.display_available_books(books)

        elif librarian_choice == 6:
            librarian.display_borrowed_books(books)

        elif librarian_choice == 7:
            continue

    elif choice == 2:
        student.show_menu()
        student_choice = int(input("Enter your choice: "))

        if student_choice == 1:
            book_id = int(input("Enter Book ID: "))
            found = False

            for book in books:
                if book.book_id == book_id:
                    student.borrow(book)
                    found = True
                    break

            if not found:
                print("Book not found.")
            else:
                save_books_to_file(books)

        elif student_choice == 2:
            book_id = int(input("Enter Book ID: "))
            found = False

            for book in books:
                if book.book_id == book_id:
                    student.return_book(book)
                    found = True
                    break

            if not found:
                print("Book not found.")
            else:
                save_books_to_file(books)

        elif student_choice == 3:
            continue

    elif choice == 3:
        teacher.show_menu()
        teacher_choice = int(input("Enter your choice: "))

        if teacher_choice == 1:
            book_id = int(input("Enter Book ID: "))
            found = False

            for book in books:
                if book.book_id == book_id:
                    teacher.borrow(book)
                    found = True
                    break

            if not found:
                print("Book not found.")
            else:
                save_books_to_file(books)

        elif teacher_choice == 2:
            book_id = int(input("Enter Book ID: "))
            found = False

            for book in books:
                if book.book_id == book_id:
                    teacher.return_book(book)
                    found = True
                    break

            if not found:
                print("Book not found.")
            else:
                save_books_to_file(books)

        elif teacher_choice == 3:
            continue