class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, year):
        new_book = Book(title, author, year)
        self.books.append(new_book)
        print(f"Book '{title}' added successfully.")

    def show_all_books(self):
        if self.books:
            print("List of all books:")
            for i, book in enumerate(self.books, 1):
                print(f"{i}. Title: {book.title}, Author: {book.author}, Year: {book.year}")
        else:
            print("No books in the list.")

    def search_book_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            print(f"Found {len(found_books)} book(s) with title '{title}':")
            for i, book in enumerate(found_books, 1):
                print(f"{i}. Title: {book.title}, Author: {book.author}, Year: {book.year}")
        else:
            print(f"No books found with title '{title}'.")



# user interface
def user_interface(book_manager):
    while True:
        print("\nMenu:")
        print("1. Add a new book")
        print("2. Show all books")
        print("3. Search a book by title")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            year = input("Enter the year of publication of the book: ")
            if not year.isdigit():
                print("Invalid input for year. Please enter a valid year.")
                continue
            book_manager.add_book(title, author, int(year))
        elif choice == '2':
            book_manager.show_all_books()
        elif choice == '3':
            title = input("Enter the title of the book you want to search: ")
            book_manager.search_book_by_title(title)
        elif choice == '4':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

book_manager = BookManager()
user_interface(book_manager)

