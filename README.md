# Personal Library & Reading Tracker

A Python-based command-line application that helps users manage their personal book collection and track their reading progress.

## 1. Project Overview

The **Personal Library & Reading Tracker** is a command-line application developed using Python. It allows users to maintain a digital record of their personal book collection, organize books by genre and reading status, monitor reading progress, and search for books using their title or author's name.

The application provides a simple and interactive CLI interface through which users can add, view, update, search, filter, and remove books from their collection.

The project uses Object-Oriented Programming (OOP) principles to organize the application logic and JSON file handling to store book information persistently.

This project is designed to demonstrate practical Python programming skills by combining fundamental concepts with real-world application development.

## 2. Project Objectives

The main objectives of this project are:

- Apply Object-Oriented Programming concepts in a practical application.
- Understand classes, objects, attributes, and methods.
- Implement composition and encapsulation where appropriate.
- Work with Python modules and packages.
- Handle user input through a command-line interface.
- Perform CRUD operations on book records.
- Implement file handling and JSON-based data persistence.
- Use lists, dictionaries, loops, conditional statements, and functions effectively.
- Implement searching and filtering functionality.
- Maintain clean, readable, and reusable Python code.

## 3. Features Implemented (Up to Lesson 6)

### 3.1 Add Books

Users can add books to their personal library by providing:

- Book title
- Author name
- Genre
- Total number of pages
- Reading status

Each book is represented as an object of the `Book` class.

### 3.2 View All Books

Users can display all books available in their personal collection.

The application displays relevant book information, including title, author, genre, total pages, reading status, and current reading progress.

### 3.3 Update Reading Progress

Users can update the current page number of a book that is being read.

This feature helps users monitor how much of a book they have completed.

### 3.4 Manage Reading Status

The application supports three reading statuses:

| Status | Description |
|---|---|
| `to-read` | Books that the user plans to read |
| `reading` | Books that the user is currently reading |
| `finished` | Books that the user has completed |

Users can mark a book as finished. The application updates its reading status and records the completion date.

### 3.5 Search Books

Users can search for books using:

- Book title
- Author name

The search functionality supports partial matching and is case-insensitive.

For example, searching for `python` can find a book titled `Python Crash Course`.

### 3.6 Filter Books

Users can filter their collection based on:

- Reading status
- Book genre

This makes it easier to organize and find specific books.

### 3.7 Remove Books

Users can remove a selected book from their personal library.

### 3.8 JSON Data Persistence

The application uses JSON file handling to store book information.

This ensures that book records remain available even after the application is closed and restarted.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core programming language |
| Object-Oriented Programming | Application structure and code organization |
| JSON | Persistent data storage |
| VS Code | Development environment |
| Git | Version control |
| GitHub | Source code hosting |

## 5. Project Structure

The project follows a modular structure to separate different application responsibilities.

```text
personal_library_and_reading_tracker/
│
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── library.py
│   ├── storage.py
│   └── cli.py
│
├── main.py
├── data.json
├── requirements.txt
├── README.md
└── .gitignore
```

### File Responsibilities

| File | Responsibility |
|---|---|
| `main.py` | Entry point of the application |
| `models.py` | Defines the Book class and book-related attributes |
| `library.py` | Handles book management operations |
| `storage.py` | Handles JSON data saving and loading |
| `cli.py` | Provides the command-line interface and user interaction |
| `data.json` | Stores book records |
| `requirements.txt` | Lists project dependencies |
| `.gitignore` | Specifies files and folders Git should ignore |
| `README.md` | Project documentation |

## 6. Application Architecture

The application is divided into separate modules, each responsible for a specific task.

The general workflow is:

```text
              User
               |
               v
          main.py
               |
               v
            cli.py
               |
               v
           library.py
               |
               v
           models.py
               |
               v
           storage.py
               |
               v
            data.json
```

**Workflow Explanation:**

1. `main.py` starts the application.
2. `cli.py` displays menu options and accepts user input.
3. `library.py` performs the requested book management operations.
4. `models.py` provides the `Book` class used to represent individual books.
5. `storage.py` handles saving and retrieving book information.
6. `data.json` stores the collection for future use.

## 7. Object-Oriented Programming Concepts

The project uses Object-Oriented Programming to improve code organization and maintainability.

### Classes and Objects

The `Book` class represents an individual book, while the `Library` class manages a collection of book objects.

### Encapsulation

Book-related attributes and operations are organized within the `Book` class, keeping the book model's responsibilities together.

### Composition

The `Library` class maintains a collection of `Book` objects.

A library contains multiple books, demonstrating a has-a relationship between the `Library` and `Book` classes.

### Modular Programming

The application is divided into multiple Python modules so that each file has a clearly defined responsibility.

## 8. Installation and Setup

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone <your-github-repository-url>
```

### Step 2: Navigate to the Project Directory

```bash
cd personal_library_and_reading_tracker
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

**macOS / Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### Step 5: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 6: Run the Application

```bash
python main.py
```

## 9. Sample CLI Menu

The application provides an interactive command-line menu.

```text
=================================
   PERSONAL LIBRARY TRACKER
=================================

1. Add a Book
2. View All Books
3. Remove a Book
4. Update Reading Progress
5. Mark Book as Finished
6. Filter Books
7. Search Books
8. Exit

Enter your choice:
```

The available menu options depend on the current CLI implementation.

## 10. Future Work

The following enhancements can be implemented to make the application more powerful, reliable, and user-friendly.

### 10.1 Advanced Validation and Exception Handling

- Implement custom exceptions for missing books and invalid operations.
- Improve validation of book details and reading progress.
- Handle corrupted JSON files gracefully.
- Provide more informative error messages.

### 10.2 Reading Statistics and Analytics

- Display the total number of books in the collection.
- Calculate books finished during the current year.
- Calculate average pages read per finished book.
- Identify the user's most-read genre.
- Provide a reading progress summary.

### 10.3 Automated Testing

- Introduce `pytest` for automated testing.
- Write unit tests for the `Book` and `Library` classes.
- Test JSON saving and loading.
- Test invalid inputs and exception handling.
- Improve application reliability through regular testing.

### 10.4 Enhanced Book Management

- Add book ratings and personal reviews.
- Support multiple authors.
- Add publication year and ISBN information.
- Allow users to sort books by title, author, genre, or reading status.

### 10.5 Data Export

- Export the personal book collection to CSV.
- Generate reading summaries in Markdown or PDF format.
- Create backup and restore functionality.

### 10.6 User Interface Improvements

- Develop a graphical user interface using Tkinter or PyQt.
- Explore building a web-based version using Flask or Django.
- Introduce a database such as SQLite or PostgreSQL for larger collections.

## 11. Learning Outcomes

Through this project, the following concepts are practised:

- Python fundamentals and core programming concepts.
- Object-Oriented Programming.
- Classes, objects, and composition.
- Functions and modular programming.
- Lists, dictionaries, and data manipulation.
- File handling and JSON serialization.
- Exception handling and input validation.
- Searching and filtering algorithms.
- Command-line application development.
- Code organization and version control.

## 12. Conclusion

The **Personal Library & Reading Tracker** demonstrates how Python fundamentals and Object-Oriented Programming can be combined to develop a practical command-line application.

The project provides an organized way to manage books, track reading progress, search and filter collections, and preserve information through JSON-based storage.

Beyond its functionality, the project serves as a practical learning experience in software development, emphasizing modular architecture, reusable code, data persistence, and problem-solving.

Future enhancements such as automated testing, advanced analytics, database integration, and graphical interfaces can further improve the application and transform it into a more complete personal reading management system.

---

**Project:** Personal Library & Reading Tracker  
**Language:** Python  
**Application Type:** Command-Line Interface (CLI)  
**Data Storage:** JSON  
**Status:** Development in Progress