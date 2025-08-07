class library:
    def __init__(self):
        self.books = []

    def add_book( self , title  , author ):
        self.books.append({'title' : title , 'author':author })
        print(f"book {title} from {title} added.")

    def remove_book(self  , title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                print(f"book {title} removed")
                return
        print(f"book {title} not found")

    def search_book(self , title):
        for book in self.books:
            if title.lower() in book['title'].lower():
                print(f"book found '{book['title']}' from '{book['author']}'")
                return
        print(f"book '{title}' not found")

    def show_books(self):
        if not self.books:
            print("There is no book available.")
        else:
            print("List of books: ")
            for book in self.books:
                print(f"-{book['title']} (author : {book{'author'}})")

