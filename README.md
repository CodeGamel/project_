------------------Library Management System-----------------------
Welcome to the Library Management System project! This command-line-based application is designed to streamline the management of books and resources within a library. The system is built using Python and demonstrates the use of Object-Oriented Programming (OOP) principles.

Project Overview
This project includes a robust Library Management System that allows users to:
Borrow and return books
Explore details about books, users, and authors

Key Features
Enhanced User Interface: A user-friendly command-line interface with separate menus for Book Operations, User Operations, and Author Operations.

Class Structure: Implemented using OOP principles with classes for Book, User, and Author.
Encapsulation: Private attributes and getter/setter methods for data access.
Error Handling: Graceful management of errors such as incorrect user input.
Optional Features: Includes bonus features like text file handling, a reservation system, and fine calculation for overdue books.
Class Structure

Book
Attributes: Title, Author, Genre, Publication Date, Availability Status
Methods: Methods to manage book details and status

User
Attributes: Name, Library ID, List of Borrowed Books
Methods: Methods to manage user details and borrowed books

Author
Attributes: Name, Biography
Methods: Methods to manage author details

----------------Installation-------------------------------
                Clone the Repository:
                
                bash
                Copy code
                git clone (https://github.com/CodeGamel/library_system1)
                cd library_system1
                Set Up Virtual Environment:
                
                bash
                Copy code
                python -m venv env
                Activate the Virtual Environment:
                
                Command Prompt:
                bash
                Copy code
                env\Scripts\activate
                PowerShell:
                powershell
                Copy code
                .\env\Scripts\Activate
                Install Dependencies:
                Ensure you have any necessary packages listed in a requirements.txt file. Install them with:
                
                bash
                Copy code
                pip install -r requirements.txt
                Usage
                Run the Application:
                
                bash
                Copy code
                python main.py
                Navigate Menus:

Follow the prompts in the command-line interface to select operations from the main menu and sub-menus.

-------------Main Menu Options--------------

        Book Operations:
        
        Add a new book
        Borrow a book
        Return a book
        Search for a book
        Display all books
        User Operations:
        
        Add a new user
        View user details
        Display all users
        Author Operations:
        
        Add a new author
        View author details
        Display all authors
        Quit: Exit the application

Feel free to fork the repository and submit pull requests. If you find any issues or have suggestions, please open an issue on GitHub.
