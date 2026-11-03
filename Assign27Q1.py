
class BookStore:

    NoOfBooks = 0

    def __init__(self):
        self.Name = ""
        self.Author = ""
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print("Enter the book name:")
        self.Name = input()

        print("Enter the author name:")
        self.Author = input()

        print("Book Name:", self.Name)
        print("Author Name:", self.Author)
        print("No of books present:", BookStore.NoOfBooks)


obj1 = BookStore()
obj1.Display()

obj2 = BookStore()
obj2.Display()

