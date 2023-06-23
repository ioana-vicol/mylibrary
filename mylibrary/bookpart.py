from books import Book

class BookPart(Book):
# initialize a subclass of "Book"
    def __init__(self, author, title, part_number):
# call the constructor of the parent class with "author" and "title"
        super().__init__(author, title)
        self.part_number = part_number

    def display(self):
#call the display-method of the parent class "Book"
        super().display()
        print(f"Part Number: {self.part_number}")

    def to_dict(self):
#call the to_dict-method of the parent class "Book"
        book_json = super().to_dict()
#return the updated "book_json"-dictionary
        book_json["part_number"] = self.part_number
        return book_json

