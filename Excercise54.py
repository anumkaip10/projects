class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        print("\n Books available in the library:")
        for book in self.books:
            print("•", book)

    def borrow_book(self, book_name):
        if book_name in self.books:
            print(f"\n You have borrowed '{book_name}'. Please return it in 7 days!")
            self.books.remove(book_name)
        else:
            print(f"\n Sorry! '{book_name}' is not available right now.")

    def return_book(self, book_name):
        print(f"\n Thank you for returning '{book_name}'.")
        self.books.append(book_name)


# --- MAIN PROGRAM ---
library = Library(["Harry Potter", "Sherlock Holmes", "Naruto Vol.1", "Python Basics"])

while True:
    print("\n=====  LIBRARY MENU =====")
    print("1. Display available books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        library.display_books()
    elif choice == '2':
        book = input("Enter the name of the book you want to borrow: ")
        library.borrow_book(book)
    elif choice == '3':
        book = input("Enter the name of the book you want to return: ")
        library.return_book(book)
    elif choice == '4':
        print("\n Thanks for visiting the library! Come again soon!")
        break
    else:
        print("\n Invalid choice! Please try again.")
