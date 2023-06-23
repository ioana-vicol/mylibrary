from books import Book
from bookseries import BookSeries
from booklibrary import BookLibrary
from User import User

if __name__ == "__main__":
    library = BookLibrary()

#create books and add them to the library
    book1 = Book("Emily Brontë", "Wuthering Heights", "Roman")
    book3 = Book("Irvin D. Yalom", "Und Nietzsche weinte", "Roman")
    book4 = Book("Michel de Montaigne", "Essais", "Philosophy")
    book2 = BookSeries("J.K. Rowling", "Harry Potter", 7, genre="Fantasy")


    library.add_book(book1.author, book1.title, book1.genre, book1.trilogy)
    library.add_book(book3.author, book3.title, book3.genre)
    library.add_book(book4.author, book4.title, book4.genre)
    library.add_book(book2.author, book2.title, book2.genre, total_parts=book2.total_parts)

#save the library data to a JSON file.
    library.save_library_to_json('library.json')

#create users
    jan = User("Jan")
    betty = User("Betty")
    angel = User("Angel")

#create a list of the user objects
    users = [jan, betty, angel]

    print("Welcome to the Book Library!")
    print()

    while True:
#user login
        user_name = input("Enter your name:")
        user = None

#iterate over the list of users
        for the_existing_user in users:
#check if the name of the current user matches with the given username
            if the_existing_user.name == user_name:
                user = the_existing_user
                break

#check if the user variable is still none
        if not user:
            print("Your User-Name was not found. Please try again.")
            continue


        while True:
#display the books in the library
            print("Books in the library:")
#check the books in the library to get the available one that that have not been obtained by any other user
            available_books = [book for book in library.books if not book.obtainedby]
            if available_books:
#iterate over all available books and show the information
                for book in available_books:
                    book.display()
                    print()
            else:
                print("There is no book available.")

#Display the menu
            print("Please select an option:")
            print("1. Search for a book")
            print("2. Display your obtained books")
            print("3. Obtain a book")
            print("4. Give a book back")
            print("5. Exit")

            print()
            select = input("Enter your choice (1-5): ").strip().lower()

            if select == "1":
                library.search_for_book()
            elif select == "2":
                user.display_the_obtained_books()
                continue

#receive a book
            elif select == "3":
                title = input("Enter the title of the book you want to obtain: ")
#create a list of books that match the title and are available
                books = [b for b in library.books if b.title == title and b.accessible]
                if books:
#select the first book from the "matching-books"-list
                    book = books[0]
                    if book.accessible:
                        if book.obtainedby:
                            print(f"The book '{book.title}' by {book.author} is already obtained by {book.obtainedby}.")
                        else:
#obtain the book for the user
                            user.obtain_book(book)
#remove the book from the library
                            library.books.remove(book)
                            book.accessible = False
                            print(f"Book '{book.title}' by {book.author} obtained.")
                    else:
                        print(f"The book '{book.title}' by {book.author}' is not available.")
                else:
                    print(f"The book '{title}' is already obtained or not found in the library.")

#give a book back
            elif select == "4":
                    title = input("Enter the title of the book you want to return: ")
                    author = input("Enter the author of the book you want to return: ")
#search for the book in the list of the user's obtained books
                    book = [b for b in user.obtained_books if b.title == title and b.author == author]
#if the book is found:
                    if book:
                        user.return_book(book[0])
                        print(f"Book '{book[0].title}' by {book[0].author} returned.")
                    else:
                        print("You do not have that book.")
#check if the user selects the number "5", or types "exit" to exit the programm
            elif select == "5" or select.lower() == "exit":
                break
            else:
                print("Invalid choice. Please try again.")


        select_exit = input("Do you want to exit the program? (Type: yes) ")
#check if the input is "yes"
        if select_exit.lower() == "yes":
            print("Goodbye!")
            break

