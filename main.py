
"""Entry point for the Personal Library application."""

from pathlib import Path

from src.cli import run_cli
from src.library import Library
from src.storage import load_books


def main() -> None:
    """Initialize and run the personal library."""

    data_file = Path(__file__).resolve().parent / "data.json"

    library = Library()

    saved_books = load_books(data_file)

    for book in saved_books:
        library.add_book(book)

    run_cli(library, data_file)


if __name__ == "__main__":
    main()
