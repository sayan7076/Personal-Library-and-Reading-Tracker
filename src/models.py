
"""Models for the Personal Library & Reading Tracker."""
# '__str__' -> method renamed as 'display' method

from datetime import date
from typing import Literal


BookStatus = Literal["to-read", "reading", "finished"] # type_alais (BookStatus) with 3 specified values as 'to-read','reading','finished'


class Book:     # 'Book' class to represent the blueprint of each books

    def __init__(  # constructor of class 'Book' with different attributes
        self,
        title: str,
        author: str,
        genre: str,
        total_pages: int,
        status: BookStatus = "to-read",    # attribute : type_alias = default_value
        current_page: int = 0,
        finish_date: date | None = None,   # either 'date' or 'None', where 'None' as default
    ) -> None:
        
        #Initializing Book object
        self.title = title
        self.author = author
        self.genre = genre
        self.total_pages = total_pages
        self.status = status
        self.current_page = current_page
        self.finish_date = finish_date

    def __str__(self) -> str:
        """Return a readable representation of the book."""

        return (
            f"Title: {self.title}\n"
            f"Author: {self.author}\n"
            f"Genre: {self.genre}\n"
            f"Total Pages: {self.total_pages}\n"
            f"Status: {self.status}\n"
            f"Current Page: {self.current_page}\n"
            f"Finish Date: {self.finish_date}"
        )
