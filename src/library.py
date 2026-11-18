
"""Library management
    Will create a 'Library' class where all the books will be stored.
    'Book' is a class itself but will use the 'Library' class to store each book with methods having functionality of 
    adding books, getting all book list, removing books.
    Summary : Library object will store Book attribute that store book object known as Composition.
    We will not use inheritance like Library(Book) because book is not library. Thats the diff in composition and inheritance."""


from src.models import Book

class Library:
    """Manage a collection of Book objects."""

    def __init__(self) -> None:  # initializing collection of books inside a list named as 'books' which will contain books with functionality same as 'Book' class

        self.books: list[Book] = [] # 'self.books' -> instance attribute || 'list[Book]' -> typehint (book list which will contain instance book object || '[]' -> empty list

    def add_book(self, book: Book) -> None: # 'book' is the attribute, 'books' is the list containing 'book' instance 

        self.books.append(book) # adding 'book' object in the 'Library' class

    def get_all_books(self) -> list[Book]: # getting all the book in a list

        return self.books.copy() # will return all the books not directly from the books list, rather will create a shallow copy 
                                 # so that original books list does not get effected 

    def remove_book(self, book: Book) -> None: # remove book from the books list

        if book not in self.books: # if -> book not present in 'books' list then 'ValueError'
            raise ValueError("Book does not exist in the library.")

        self.books.remove(book) # else -> book present then removing it from the 'books' list
