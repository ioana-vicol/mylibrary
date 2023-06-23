from books import Book

class BookSeries(Book):
    def __init__(self, author, title, total_parts, genre=None, trilogy=None):
#call the init-method of the parent class "Book", and give the necessary arguments
        super().__init__(author, title, genre, trilogy)
        self.total_parts = total_parts
#initialize an empty dictionary to store the parts of the BookSeries
        self.parts = {}

    def add_part(self, part_number, part_title):
#Assign the part_title to the part_number in the parts-dictionary
        self.parts[part_number] = part_title

#Show the BookSeries information
    def display(self):
        #Call the "display"-method of the parent class "Book"
        super().display()
        print(f"Total Parts: {self.total_parts}")
        if self.parts:
            print("Parts:")
#Iterate over the parts dictionary and display the part number and der part title
            for part_number, part_title in self.parts.items():
                print(f"  Part {part_number}: {part_title}")

#Convert the informations to a dictionary
    def to_dict(self):
        data = super().to_dict()
#Add the "total_parts" and the "parts" attributes to the dictionary
        data["total_parts"] = self.total_parts
        data["parts"] = self.parts
        return data

