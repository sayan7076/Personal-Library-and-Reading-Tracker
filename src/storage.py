
"""Handle JSON storage for the personal library."""

import json
from datetime import date
from pathlib import Path
from typing import Any

from src.models import Book


def _book_to_dict(book: Book) -> dict[str, Any]:
    """Convert a Book object into a JSON-compatible dictionary."""

    return {
        "title": book.title,
        "author": book.author,
        "genre": book.genre,
        "total_pages": book.total_pages,
        "status": book.status,
        "current_page": book.current_page,
        "finish_date": (
            book.finish_date.isoformat()
            if book.finish_date is not None
            else None
        ),
    }


def _dict_to_book(data: dict[str, Any]) -> Book:
    """Convert a dictionary into a Book object."""

    finish_date_text = data["finish_date"]

    finish_date = (
        date.fromisoformat(finish_date_text)
        if finish_date_text is not None
        else None
    )

    return Book(
        title=data["title"],
        author=data["author"],
        genre=data["genre"],
        total_pages=data["total_pages"],
        status=data["status"],
        current_page=data["current_page"],
        finish_date=finish_date,
    )


def save_books(books: list[Book], file_path: Path) -> None:
    """Save a list of Book objects into a JSON file."""

    file_path.parent.mkdir(parents=True, exist_ok=True)

    data = [_book_to_dict(book) for book in books]

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_books(file_path: Path) -> list[Book]:
    """Load Book objects from a JSON file."""

    if not file_path.exists():
        return []

    with file_path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return [_dict_to_book(item) for item in data]


# import os
# import json
# from datetime import date
# from pathlib import Path
# from src.models import Book

# FILENAME = "data/books.json"


# def ensure_file_exists() -> None:
#     os.makedirs(os.path.dirname(FILENAME), exist_ok=True)

#     if not os.path.exists(FILENAME):
#         with open(FILENAME, "x", encoding="utf-8") as f:
#             json.dump([], f, indent=4)


# def read_data() -> list[Book]:
#     with open(FILENAME, "r", encoding="utf-8") as f:
#         books = list(json.load(f))

#         return [
#             Book(
#                 title=book["title"],
#                 author=book["author"],
#                 genre=book["genre"],
#                 total_pages=book["total_pages"],
#                 status=book["status"],
#                 current_page=book["current_page"],
#                 finish_date=date.fromisoformat(book["finish_date"])
#                 if book["finish_date"] is not None else None
#             )
#             for book in books
#         ]


# def write_data(books: list[Book]) -> None:
#     serialized_books = [
#         {
#             "title": book.title,
#             "author": book.author,
#             "genre": book.genre,
#             "total_pages": book.total_pages,
#             "status": book.status,
#             "current_page": book.current_page,
#             "finish_date": book.finish_date.isoformat()
#             if book.finish_date is not None else None
#         }
#         for book in books
#     ]

#     with open(FILENAME, "w", encoding="utf-8") as f:
#         json.dump(serialized_books, f, indent=4, ensure_ascii=False)
