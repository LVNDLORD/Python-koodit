from abc import ABC, abstractmethod


class Publication(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def print_information(self):
        pass


class Book(Publication):

    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        print(f"{self.name} ({self.author}, {self.page_count} pages) ")


class Magazine(Publication):

    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_ed = chief_editor

    def print_information(self):
        print(f"{self.name} (chief editor {self.chief_ed})")


if __name__ == '__main__':

    mag = Magazine("Donald Duck", "Aki Hyyppä")
    book = Book("Compartment No. 6", "author Rosa Liksom", 192)
    mag.print_information()
    book.print_information()