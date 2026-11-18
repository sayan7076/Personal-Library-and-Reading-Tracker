
"""Demonstrate Library operations."""

from src.models import Book
from src.library import Library


def main() -> None:
    """Run a demonstration of the Library class."""

    library = Library()

    book1 = Book(
        "Atomic Habits",
        "James Clear",
        "Self-help",
        320
    )

    book2 = Book(
        "Python Crash Course",
        "Eric Matthes",
        "Programming",
        560
    )

    # Add books
    library.add_book(book1)
    library.add_book(book2)

    # View books
    print("All Books:")

    for book in library.get_all_books():
        print(book.title)

    # Remove a book
    library.remove_book(book1)

    print("\nAfter removing Atomic Habits:")

    for book in library.get_all_books():
        print(book.title)


if __name__ == "__main__":
    main()
