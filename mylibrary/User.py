import json

class User:
    def __init__(self, name):
        self.name = name
        self.obtained_books = []

    def obtain_book(self, book):
#check if the book is available, update the availability, and assign the user's name to the "obtainedby"-attribute.
        if book.accessible:
            book.accessible = False
            book.obtainedby = self.name
            self.obtained_books.append(book)

    def return_book(self, book):
        #remove the book from the user's obtained books-list. Update the "obtainedby" and the availability status.
        self.obtained_books.remove(book)
        book.obtainedby = None
        book.accessible = True

    def display_the_obtained_books(self):
#show the user's obtained books
        if self.obtained_books:
            print("Obtained Books:")
#iterate trough the list of the obtained books
            for book in self.obtained_books:
                book.display()
                print()
        else:
            print("You have not obtained any book.")

    def save_books_to_json(self):
#create the data dictionary with the received books and save them to the JSON file
        data = {"obtained_books": [book.to_dict() for book in self.obtained_books]}
        with open(f"{self.name}_books.json", "w") as file:
            json.dump(data, file)

    def load_books_from_json(self):
        try:
#open the JSON file
            with open(f"{self.name}_books.json", "r") as file:
#load the data from the JSON file
                data = json.load(file)
#create a list of 'Book'-objects through iterating over the obtained book data.
                self.obtained_books = [Book(book_data["author"], book_data["title"], book_data["genre"],
                                           book_data["trilogy"]) for book_data in data["obtained_books"]]
        except FileNotFoundError:
            self.obtained_books = []

