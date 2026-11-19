

"""Command-line interface for the personal library."""

from datetime import date
from pathlib import Path
from typing import cast

from src.library import Library
from src.models import Book, BookStatus
from src.storage import save_books


def _add_book(library: Library, data_file: Path) -> None:
    """Collect book details and add a new book."""

    print("\n--- Add a New Book ---")

    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    genre = input("Enter genre: ").strip()

    if not title or not author or not genre:
        print("Title, author and genre cannot be empty.")
        return

    try:
        total_pages = int(input("Enter total pages: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return

    if total_pages <= 0:
        print("Total pages must be greater than zero.")
        return

    status_text = input(
        "Enter status (to-read/reading/finished): "
    ).strip().lower()

    if not status_text:
        status_text = "to-read"

    if status_text not in ("to-read", "reading", "finished"):
        print("Invalid reading status.")
        return

    status = cast(BookStatus, status_text)

    current_page = total_pages if status == "finished" else 0

    finish_date = (
        date.today() if status == "finished" else None
    )

    book = Book(
        title=title,
        author=author,
        genre=genre,
        total_pages=total_pages,
        status=status,
        current_page=current_page,
        finish_date=finish_date,
    )

    library.add_book(book)

    save_books(library.get_all_books(), data_file)

    print(f"'{title}' added successfully!")


def _view_books(library: Library) -> None:
    """Display all books in the library."""

    print("\n--- Your Book Collection ---")

    books = library.get_all_books()

    if not books:
        print("Your library is empty.")
        return

    for index, book in enumerate(books, start=1):
        print(f"\nBook Number: {index}")
        print(book)
        print("-" * 35)


def _remove_book(library: Library, data_file: Path) -> None:
    """Remove a selected book from the library."""

    books = library.get_all_books()

    if not books:
        print("Your library is empty.")
        return

    _view_books(library)

    try:
        book_number = int(
            input("Enter the book number to remove: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return

    if book_number < 1 or book_number > len(books):
        print("Invalid book number.")
        return

    selected_book = books[book_number - 1]

    library.remove_book(selected_book)

    save_books(library.get_all_books(), data_file)

    print(f"'{selected_book.title}' removed successfully!")


def run_cli(library: Library, data_file: Path) -> None:
    """Run the main command-line menu."""

    while True:

        print("\n==============================")
        print("       PERSONAL LIBRARY")
        print("==============================")

        print("1. Add a book")
        print("2. View all books")
        print("3. Remove a book")
        print("4. Exit")

        choice = input("\nEnter your choice: ").strip()

        match choice:

            case "1":
                _add_book(library, data_file)

            case "2":
                _view_books(library)

            case "3":
                _remove_book(library, data_file)

            case "4":
                print("Thank you for using Personal Library!")
                break

            case _:
                print("Invalid choice. Please try again.")




# """Command-line interface for the personal library."""

# from datetime import date

# from src.library import Library
# from src.models import Book, BookStatus
# from src.storage import save_books


# MENU_OPTIONS = ("Add a book", "View all books", "Remove a book", "Exit",)


# def get_menu() -> str:
#     menu = "\n--- PERSONAL LIBRARY CLI ---\n"

#     for idx, val in enumerate(MENU_OPTIONS):
#         menu += f"⦿ {idx + 1} - {val}\n"

#     return menu


# def add_book(library: Library, data_file) -> None:

#     print("\n--- Add a New Book ---")

#     title = input("Enter book title: ").strip()
#     author = input("Enter author name: ").strip()
#     genre = input("Enter genre: ").strip()

#     # title, author, genre (should not be empty)
#     if not title or not author or not genre:
#         print("Title, author and genre cannot be empty.")
#         return

#     # total_pages (should be number and grater than 0)
#     try:
#         total_pages = int(input("Enter total pages: "))
#     except ValueError:
#         print("Please enter a valid whole number.")
#         return
#     if total_pages <= 0:
#         print("Total pages must be greater than zero.")
#         return

#     # status in default 'to-read', get changed according to the status
#     status = input(
#         "Enter status (to-read/reading/finished): "
#     ).strip().lower()
#     if status == "":
#         status = "to-read"
#     elif status == "to-read":
#         status = "to-read"
#     elif status == "reading":
#         status = "reading"
#     elif status == "finished":
#         status = "finished"
#     else:
#         print("Invalid reading status.")
#         return

#     # if book status is 'finished' then current_page will be the last page i.e. 'total_page'
#     current_page = total_pages if status == "finished" else 0

#     # add today's date if user add book with status 'finished'
#     finish_date = date.today() if status == "finished" else None

#     book = Book(
#         title=title,
#         author=author,
#         genre=genre,
#         total_pages=total_pages,
#         status=status,
#         current_page=current_page,
#         finish_date=finish_date
#     )

#     library.add_book(book)

#     save_books(library.get_all_books(), data_file)

#     print(f"'{title}' added successfully!")


# def view_books(library: Library) -> None:

#     print("\n--- Your Book Collection ---")

#     books = library.get_all_books()

#     if not books:
#         print("Your library is empty.")
#         return

#     for idx, book in enumerate(books, start=1):
#         print(f"\nBook Number: {idx}")
#         print(book)
#         print("-" * 35)


# def remove_book(library: Library, data_file) -> None:

#     books = library.get_all_books()

#     if not books:
#         print("Your library is empty.")
#         return

#     view_books(library)

#     try:
#         book_number = int(input("Enter the book number to remove: "))
#     except ValueError:
#         print("Please enter a valid number.")
#         return

#     if book_number < 1 or book_number > len(books):
#         print("Invalid book number.")
#         return

#     selected_book = books[book_number - 1]

#     library.remove_book(selected_book)

#     save_books(library.get_all_books(), data_file)

#     print(f"'{selected_book.title}' removed successfully!")


# def run_cli(library: Library, data_file) -> None:

#     while True:

#         print(get_menu())

#         choice = input("Enter your choice: ").strip()

#         match choice:

#             case "1":
#                 add_book(library, data_file)

#             case "2":
#                 view_books(library)

#             case "3":
#                 remove_book(library, data_file)

#             case "4":
#                 print("Thank you for using Personal Library!")
#                 break

#             case _:
#                 print("Invalid choice. Please try again.")
