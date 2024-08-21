from book_sql import add_book, borrow_book, return_book
from book_sql import search_book, display_library
from users_sql import add_user, view_user_details, display_users
from  authors_sql import add_author, view_author_details, display_authors
import mysql.connector
from mysql.connector import Error
from db_connect import connect_db
from datetime import datetime

class LibraryManagementSystem:
    def __init__(self):
        self.db_name = 'module5db'
        self.user = 'root'
        self.password = 'Steamisbetter11-'
        self.host = 'localhost'
        self.conn = None
        self.cursor = None

    class Author:
        def __init__(self, name, biography):
            self.__name = name
            self.__biography = biography

        def get_name(self):
            return self.__name

        def display_info(self):
            print(f"Name: {self.__name}")
            print(f"Biography: {self.__biography}")


    class User:
        def __init__(self, name, library_id):
            self.__name = name
            self.__library_id = library_id
            self.__borrowed_books = []

        def get_library_id(self):
            return self.__library_id

        def get_name(self):
            return self.__name

        def get_borrow_book(self, book_title, due_date):
            self.__borrowed_books.append({"title": book_title, "due_date": due_date})

        def return_book(self, book_title):
            for book in self.__borrowed_books:
                if book["title"] == book_title:
                    self.__borrowed_books.remove(book)
                    return

        def display_info(self):
            print(f"Name: {self.__name}")
            print(f"Library ID: {self.__library_id}")
            print("Borrowed Books:")
            for book in self.__borrowed_books:
                print(f"- {book['title']} (Due: {book['due_date']})")

    class BookOperations:
        def __init__(self, title, author, genre, publication_date):
            self.title = title
            self.author = author
            self.genre = genre
            self.publication_date = publication_date
            self.is_borrowed = False
        
        def is_available(self):
            return not self.is_borrowed

        def set_availability(self, available):
            self.is_borrowed = not available

        def display_info(self):
            print(f"Title: {self.title}")
            print(f"Author: {self.author}")
            print(f"Genre: {self.genre}")
            print(f"Publication Date: {self.publication_date}")
            print(f"Status: {'Borrowed' if self.is_borrowed else 'Available'}")

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                database=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host
            )
            if self.conn.is_connected():
                print("Connection to MySQL database successful!")
                self.cursor = self.conn.cursor()
        except Error as e:
            print(f"Error: {e}")

    def close_connection(self):
        if self.conn and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Connection successfully closed!")

    
    def main_menu(self):
            connect_db()
            while True:
                selection = input('''
            Welcome to the Library Management System with Database Integration!
            ******************
            Main Menu:
            1. Book Operations
            2. User Operations
            3. Author Operations
            4. Quit
            
        
            ''')

                if selection == '1':
                    self.book_menu()
                elif selection == '2':
                    self.user_menu()
                elif selection == '3':
                    self.author_menu()
                elif selection == '4':
                    print("Thanks for using the Library Management System!")
                    break
                else:
                    print ('Invalid Entry.')

        
    def book_menu(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                add_book() 
            elif choice == '2':
                borrow_book()
            elif choice == '3':
                return_book()
            elif choice == '4':
                search_book()
            elif choice == '5':
                display_library()
            elif choice == '6':
                break
            else:
                print ('Invalid Entry.')

    def user_menu(self):
        while True:
            
            print("User Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                add_user()
            elif choice == '2':
                view_user_details()
                print('-'*40)
            elif choice == '3':
                display_users()
                print('-'*40)
            elif choice == '4':
                break
            else:
                print ('Invalid Entry.')

    def author_menu(self):
        while True:
                
            print("Author Operations:")
            
            print("1. Add a new author")
            
            print("2. View author details")
            
            print("3. Display all authors")
            
            print("4. Back to Main Menu")
            choice = input("Enter your choice: ")

            if choice == '1':
                add_author()
            elif choice == '2':

                view_author_details()
            elif choice == '3':
                display_authors()

            elif choice == '4':
                break
            else:
                print ('Invalid Entry.')
                
if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.connect()
    try:
        system.main_menu()
    finally:
        system.close_connection()
