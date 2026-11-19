
"""Library management
    Will create a 'Library' class where all the books will be stored.
    'Book' is a class itself but will use the 'Library' class to store each book with methods having functionality of 
    adding books, getting all book list, removing books.
    Summary : Library object will store Book attribute that store book object known as Composition.
    We will not use inheritance like Library(Book) because book is not library. Thats the diff in composition and inheritance."""


# from src.models import Book

# class Library:
#     """Manage a collection of Book objects."""

#     def __init__(self) -> None:  # initializing collection of books inside a list named as 'books' which will contain books with functionality same as 'Book' class

#         self.books: list[Book] = [] # 'self.books' -> instance attribute || 'list[Book]' -> typehint (book list which will contain instance book object || '[]' -> empty list

#     def add_book(self, book: Book) -> None: # 'book' is the attribute, 'books' is the list containing 'book' instance 

#         self.books.append(book) # adding 'book' object in the 'Library' class

#     def get_all_books(self) -> list[Book]: # getting all the book in a list

#         return self.books.copy() # will return all the books not directly from the books list, rather will create a shallow copy 
#                                  # so that original books list does not get effected 

#     def remove_book(self, book: Book) -> None: # remove book from the books list

#         if book not in self.books: # if -> book not present in 'books' list then 'ValueError'
#             raise ValueError("Book does not exist in the library.")

#         self.books.remove(book) # else -> book present then removing it from the 'books' list


"""Library management logic."""

from datetime import date

from src.models import Book, BookStatus


class Library:
    """Manage a collection of Book objects."""

    def __init__(self) -> None:
        """Initialize an empty library."""

        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a Book object to the library."""

        self.books.append(book)

    def get_all_books(self) -> list[Book]:
        """Return all books in the library."""

        return self.books.copy()

    def remove_book(self, book: Book) -> None:
        """Remove a Book object from the library."""

        if book not in self.books:
            raise ValueError("Book does not exist in the library.")

        self.books.remove(book)

    # def update_progress(
    #     self,
    #     book: Book,
    #     current_page: int
    # ) -> None:
    #     """Update the reading progress of a book."""

    #     if book not in self.books:
    #         raise ValueError("Book does not exist in the library.")

    #     if book.status != "reading":
    #         raise ValueError("Only reading books can be updated.")

    #     if not 0 <= current_page < book.total_pages:
    #         raise ValueError(
    #             f"Page must be between 0 and {book.total_pages - 1}."
    #         )

    #     book.current_page = current_page

    
    def update_progress(
        self,
        book: Book,
        current_page: int
    ) -> None:
        """Update the reading progress of a book."""

        if book not in self.books:
            raise ValueError("Book does not exist in the library.")

        if book.status == "finished":
            raise ValueError("Finished books cannot be updated.")

        if not 0 <= current_page < book.total_pages:
            raise ValueError("Invalid page number.")

        # Automatically change status to reading
        book.status = "reading"

        # Update current reading page
        book.current_page = current_page

    
    def mark_finished(self, book: Book) -> None:
        """Mark a book as finished and record its finish date."""

        if book not in self.books:
            raise ValueError("Book does not exist in the library.")

        if book.status == "finished":
            raise ValueError("This book is already finished.")

        book.status = "finished"
        book.current_page = book.total_pages
        book.finish_date = date.today()

    def get_books_by_status(
        self,
        status: BookStatus
    ) -> list[Book]:
        """Return books matching the given reading status."""

        return [
            book for book in self.books
            if book.status == status
        ]

    def get_books_by_genre(self, genre: str) -> list[Book]:
        """Return books matching the given genre."""

        return [
            book for book in self.books
            if book.genre.casefold() == genre.casefold()
        ]

    def search_books(self, search_term: str) -> list[Book]:
        """Search books by partial title or author match."""

        search_term = search_term.strip().casefold()

        if not search_term:
            return []

        return [
            book for book in self.books
            if search_term in book.title.casefold()
            or search_term in book.author.casefold()
        ]
