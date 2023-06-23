class Book:
    def __init__(self, author, title, genre=None, trilogy=None):
        self.author = author
        self.title = title
        self.genre = genre
        self.trilogy = trilogy
        self.obtainedby = None
        self.accessible = True

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        if self.genre:
            print(f"Genre: {self.genre}")
        if self.trilogy:
            print(f"Trilogy: {self.trilogy}")

    def to_dict(self):
            return {
                "author": self.author,
                "title": self.title,
                "genre": self.genre,
                "trilogy": self.trilogy,
                "obtained by": self.obtainedby,
                "accessible": self.accessible
            }