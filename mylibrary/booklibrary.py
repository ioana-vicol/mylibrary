import json
import random
from books import Book
from bookseries import BookSeries

class BookLibrary:
#initialize the BookLibrary
    def __init__(self):
        self.books = []

    def add_book(self, author, title, genre=None, trilogy=None, total_parts=None):
#check if the book is a part of a series
        if trilogy and total_parts:
            book = BookSeries(author, title, total_parts, genre, trilogy)
        else:
            book = Book(author, title, genre)
        self.books.append(book)

#Delete a book from the library
    def delete_book(self, author, title):
#Iterate over the books in the library
        for book in self.books:
#check if the book's title and author match the provided title and author
            if book.title == title and book.author == author:
                self.books.remove(book)
                print(f"Book {title} by {author} removed from the library.")
                return
        print(f"Book {title} by {author} not found in the library.")

    def search_for_book(self):
        while True:
            genre_author = input("Search by genre/author or do you want a suggested book?")
#Create an empty list to store the matching books
            books_for_genreauthor = []


            if genre_author == "genre":
                abfrage = input("Enter your genre:")
#Filter the books by "genre"
                books_for_genreauthor = [book for book in self.books if book.genre == abfrage]
#If there are books in the books_for_genreauthor-list:
                if books_for_genreauthor:
                    print("Book/s found:")
                    for book in  books_for_genreauthor:
                        book.display()
                        print()
                else:
                    print("No matching books found. Try again")


            elif genre_author == "author":
                abfrage = input("Enter your author:")
                books_for_genreauthor = [book for book in self.books if book.author == abfrage]

                if books_for_genreauthor:
                    print("Book/s found:")
                    for book in books_for_genreauthor:
                        book.display()
                    print()
                else:
                    print("No matching books found. Try again")

            elif genre_author == "suggested":
#Show a random suggested book
                self.suggested_book()
            else:
                print("Invalid search type")

            break

    def suggested_book(self):
#if the "self.books"-list is empty, return
        if not self.books:
            return
#choose a random book from the "self.books"-list
        random_book = random.choice(self.books)
        print("Suggested book: ")
        random_book.display()

    def books_accessible(self):
#return a list that filters the books in the "self.books"-list based on the accessibility.
        return [book for book in self.books if not book.obtainedby]


    def save_library_to_json(self, filename):
#create a dictionary to store the data
        data = {"books": [book.to_dict() for book in self.books]}
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_library_from_file(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.books = []
#iterate over all data in the JSON data
                for book_data in data["books"]:
                    if "total_parts" in book_data:
#create the object BookSeries
                        book = BookSeries(
                            book_data["author"],
                            book_data["title"],
                            book_data["total_parts"],
                            book_data["genre"],
                            book_data["trilogy"]
                        )
                        for part_data in book_data["parts"]:
#create the object "BookPart" and append it to the parts
                            part = BookPart(
                                book_data["author"],
                                part_data["title"],
                                part_data["part_number"]
                            )
                            book.parts.append(part)
                    else:
                        book = Book(
                            book_data["author"],
                            book_data["title"],
                            book_data["genre"],
                            book_data["trilogy"]
                        )
                    book.obtained_by = book_data["obtained_by"]
                    book.accessible = book_data["accessible"]
#Append the book to the "self.books"-list
                    self.books.append(book)
            print(f"Library data loaded from {filename}.")
        except FileNotFoundError:
            print(f"Library data file {filename} not found.")

