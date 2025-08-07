class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        self.is_available = False

    def return_book(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"{self.title} by {self.author} - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        print("✅ Book added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("🗑️ Book removed successfully.")
                return
        print("❌ Book not found.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print("🔍 Book found:", book)
                return
        print("❌ Book not found.")

    def display_books(self):
        if not self.books:
            print("📚 Library is empty.")
        else:
            print("📘 List of Books:")
            for book in self.books:
                print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_available:
                    book.borrow()
                    print("✅ You have borrowed the book.")
                else:
                    print("⚠️ Book is already borrowed.")
                return
        print("❌ Book not found.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_available:
                    book.return_book()
                    print("✅ Book returned successfully.")
                else:
                    print("⚠️ This book wasn't borrowed.")
                return
        print("❌ Book not found.")


def main():
    library = Library()

    while True:
        print("\n========= LIBRARY MENU =========")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Borrow Book")
        print("6. Return Book")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == '2':
            title = input("Enter book title to remove: ")
            library.remove_book(title)

        elif choice == '3':
            title = input("Enter book title to search: ")
            library.search_book(title)

        elif choice == '4':
            library.display_books()

        elif choice == '5':
            title = input("Enter book title to borrow: ")
            library.borrow_book(title)

        elif choice == '6':
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == '0':
            print("👋 Exiting... Thank you!")
            break

        else:
            print("❗ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
