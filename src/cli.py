
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


def _display_books(books: list[Book]) -> None:
    """Display a list of books."""

    if not books:
        print("No books found.")
        return

    for index, book in enumerate(books, start=1):
        print(f"\nBook Number: {index}")
        print(book)
        print("-" * 35)


def _view_books(library: Library) -> None:
    """Display all books in the library."""

    print("\n--- Your Book Collection ---")

    books = library.get_all_books()

    if not books:
        print("Your library is empty.")
        return

    _display_books(books)


def _select_book(library: Library) -> Book | None:
    """Let the user select a book from the library."""

    books = library.get_all_books()

    if not books:
        print("Your library is empty.")
        return None

    _display_books(books)

    try:
        book_number = int(
            input("\nEnter book number: ")
        )
    except ValueError:
        print("Please enter a valid number.")
        return None

    if not 1 <= book_number <= len(books):
        print("Invalid book number.")
        return None

    return books[book_number - 1]


def _remove_book(library: Library, data_file: Path) -> None:
    """Remove a selected book from the library."""

    selected_book = _select_book(library)

    if selected_book is None:
        return

    library.remove_book(selected_book)

    save_books(library.get_all_books(), data_file)

    print(f"'{selected_book.title}' removed successfully!")


def _update_progress(
    library: Library,
    data_file: Path
) -> None:
    """Update the reading progress of a selected book."""

    selected_book = _select_book(library)

    if selected_book is None:
        return

    try:
        current_page = int(
            input("Enter your current page: ")
        )
    except ValueError:
        print("Please enter a valid whole number.")
        return

    try:
        library.update_progress(selected_book, current_page)
    except ValueError as error:
        print(f"Could not update progress: {error}")
        return

    save_books(library.get_all_books(), data_file)

    print("Reading progress updated successfully!")


def _mark_finished(
    library: Library,
    data_file: Path
) -> None:
    """Mark a selected book as finished."""

    selected_book = _select_book(library)

    if selected_book is None:
        return

    try:
        library.mark_finished(selected_book)
    except ValueError as error:
        print(f"Could not finish book: {error}")
        return

    save_books(library.get_all_books(), data_file)

    print(f"'{selected_book.title}' marked as finished!")


def _filter_books(library: Library) -> None:
    """Filter books by reading status or genre."""

    print("\n--- Filter Books ---")
    print("1. Filter by status")
    print("2. Filter by genre")

    choice = input("Enter your choice: ").strip()

    if choice == "1":

        status = input(
            "Enter status (to-read/reading/finished): "
        ).strip().lower()

        if status not in ("to-read", "reading", "finished"):
            print("Invalid reading status.")
            return

        filtered_books = library.get_books_by_status(
            cast(BookStatus, status)
        )

    elif choice == "2":

        genre = input("Enter genre: ").strip()

        if not genre:
            print("Genre cannot be empty.")
            return

        filtered_books = library.get_books_by_genre(genre)

    else:
        print("Invalid filter choice.")
        return

    _display_books(filtered_books)


def _search_books(library: Library) -> None:
    """Search books by title or author."""

    search_term = input(
        "Enter title or author to search: "
    ).strip()

    if not search_term:
        print("Search term cannot be empty.")
        return

    results = library.search_books(search_term)

    print("\n--- Search Results ---")

    _display_books(results)


def run_cli(library: Library, data_file: Path) -> None:
    """Run the main command-line menu."""

    while True:

        print("\n==============================")
        print("       PERSONAL LIBRARY")
        print("==============================")

        print("1. Add a book")
        print("2. View all books")
        print("3. Remove a book")
        print("4. Update reading progress")
        print("5. Mark a book as finished")
        print("6. Filter books")
        print("7. Search books")
        print("8. Exit")

        choice = input("\nEnter your choice: ").strip()

        match choice:

            case "1":
                _add_book(library, data_file)

            case "2":
                _view_books(library)

            case "3":
                _remove_book(library, data_file)

            case "4":
                _update_progress(library, data_file)

            case "5":
                _mark_finished(library, data_file)

            case "6":
                _filter_books(library)

            case "7":
                _search_books(library)

            case "8":
                print("Thank you for using Personal Library!")
                break

            case _:
                print("Invalid choice. Please try again.")
