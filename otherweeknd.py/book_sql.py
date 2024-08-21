import mysql.connector
from mysql.connector import Error
from db_connect import connect_db
from datetime import datetime
import random
from tabulate import tabulate

def add_book():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()
            title = input("Please enter the name of the book: ")
            author = input ("Enter the Author: ")
            publication_date = input("Enter the publication date: (MM/DD/YYYY) ")
            isbn = ''.join([str(random.randint(0, 9)) for _ in range(13)])
    
    
            isbn = f"{isbn[:3]}-{isbn[3:4]}-{isbn[4:8]}-{isbn[8:12]}-{isbn[12]}"
            try:
                date_ = datetime.strptime(publication_date, '%m/%d/%Y')
                formatted_date = date_.strftime('%Y-%m-%d')
            except ValueError:
                print("Invalid date format. Please use MMDDYYYY.")
                return
            
            new_book = (title, author, isbn, formatted_date)

            query = "INSERT INTO books (title, author, isbn, publication_date) VALUES (%s, %s, %s, %s)"

            cursor.execute(query, new_book)
            conn.commit()
            print('Book added to library')
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def borrow_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            book_id = input("Enter the name of the book you'd like to borrow: ")
            user_id = input("Please enter your library id: ")
            borrow_date = input("Enter todays date: ")
            return_date = input("Enter the date of when you must return the book: ")
            borrow_date_obj = datetime.strptime(borrow_date, '%m/%d/%Y')
            return_date_obj = datetime.strptime(return_date, '%m/%d/%Y')
    
    # Format the dates for output
            formatted_borrow_date = borrow_date_obj.strftime('%Y/%m/%d')
            formatted_return_date = return_date_obj.strftime('%Y/%m/%d')
    
            print(f"Book ID: {book_id}")
            print(f"User ID: {user_id}")
            print(f"Borrow Date: {formatted_borrow_date}")
            print(f"Return Date: {formatted_return_date}")

            
            # Log the borrow 
            log_query = "INSERT INTO borrowed_books (book_id, user_id, borrow_date, return_date) VALUES (%s, %s, %s,%s)"
            cursor.execute(log_query, (book_id, user_id, formatted_borrow_date, formatted_return_date,))
            conn.commit()
            print(f"The book {book_id} has been borrowed, and must be returned by {borrow_date}.")
            

        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def return_book():
    conn = connect_db()
    if conn is not None:
        try:
            print(f"{book_id}")
            book_id = input(f"Please enter the book id your will like to return: ")
            cursor = conn.cursor()

            query = "UPDATE books SET availability = True WHERE id = %s" 

            cursor.execute(query,(book_id,))
            conn.commit()

            select_query = "SELECT * FROM books WHERE id = %s "
            cursor.execute(select_query, (book_id,))
        

            id, title, author_id, isbn, publication_date, availability = cursor.fetchone()
           
            print(f"{title} book, under {id} was returned successfully")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close() # NEVER FORGET
            print("Connection successfully close")
            

def search_book():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            book_title = input("Enter the title of the book you are searching for: ")

            # Query to search for the book by title
            search_query = """
                SELECT id, title, author, isbn, publication_date, availability 
                FROM books 
                WHERE title = %s
            """
            cursor.execute(search_query, (book_title,))
            result = cursor.fetchone()

            if result is None:
                print("Book not found.")
                return
        
            # Extracting book details from the result
            book_id, title, author, isbn, publication_date, availability = result

            # Format the publication date
            formatted_date = publication_date.strftime('%m/%d/%Y') if publication_date else 'N/A'

            # Display the book details
            print(f"Book ID: {book_id}")
            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"ISBN: {isbn}")
            print(f"Publication Date: {formatted_date}")
            print(f"Availability: {'Available' if availability else 'Not Available'}")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

    
def display_library():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            fetch_query = "SELECT id, title, author, isbn, publication_date, availability FROM books;"
            cursor.execute(fetch_query)
            rows = cursor.fetchall()

            # Format the rows for tabulate
            formatted_rows = []
            for row in rows:
                book_id, title, author, isbn, publication_date, availability = row
                formatted_date = publication_date.strftime('%m/%d/%Y') if publication_date else 'N/A'
                availability_status = 'Available' if availability else 'Not Available'
                formatted_rows.append([book_id, title, author, isbn, formatted_date, availability_status])

            # Define column headers
            headers = ["ID", "Title", "Author", "ISBN", "Publication Date", "Availability"]

            # Print the table using tabulate
            print(tabulate(formatted_rows, headers=headers, tablefmt="grid"))

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

