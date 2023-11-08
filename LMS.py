class Library:
    def __init__(self):
        self.nobooks = 0
        self.books = []

    def addBook(self, *book):
        self.books.extend(list(book))
        self.nobooks = len(self.books)

    def showInfo(self, info="both"):
        if (info == "book"):
            print(f"The books in the library are {self.books}")
        elif (info == "no"):
            print(f"The no. of books in the library are {self.nobooks}")
        elif (info == "both"):
            print(f"The no. of books in the library are {self.nobooks}")
            print(f"The books in the library are {self.books}")
        else:
            print(f"The no. of books in the library are {self.nobooks}")
            print(f"The books in the library are {self.books}")


l1 = Library()
l1.addBook("HP1", "HP2")
l1.showInfo("no")
