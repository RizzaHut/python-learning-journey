class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        return


class Library:
    def __init__(self, name: str,) -> None:
        self.name = name
        self.books = []
        return

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        

    def remove_book(self, book: Book) -> None:
        self.book = book
        saved_book = []

        for b in self.books:
            if b.title != book.title or b.author != book.author:
                saved_book.append(b)
        self.books = saved_book
        return

    def search_books(self, search_string: str) -> list[Book]:
        search_query = search_string.lower()
        search_result = []

        for b in self.books:
            if search_query in b.title.lower() or search_query in b.author.lower():
                search_result.append(b)
        return search_result
