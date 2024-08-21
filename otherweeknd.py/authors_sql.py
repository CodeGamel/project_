from db_connect import connect_db
import mysql.connector
from mysql.connector import Error
from tabulate import tabulate

def add_author():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("What is the Author's name?").title()
            biography = input("Write something about this Author.")

            new_author = (name,biography)

            query = "INSERT INTO authors (name, biography) VALUES (%s, %s)"

            cursor.execute(query, new_author)
            conn.commit()
            print('New Author added succesfully!')
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
if __name__ == "__main__":
    add_author()


def display_authors():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Selecting all authors
            fetch_query = "SELECT * FROM authors;"
            cursor.execute(fetch_query)
           
            for row in cursor.fetchall():
                print (row)
                print('-'*40)
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
if __name__ == "__main__":
    display_authors()
    
def view_author_details():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()
            author_name = input("Enter Author ID: ")
            # Query to select details for a specific author
            fetch_query = "SELECT * FROM authors WHERE name  = %s;"
            cursor.execute(fetch_query, (author_name,))
            row = cursor.fetchone()
            if row is None:
                print("This author can not be found.")
            elif row:
                id, name, biography = row
                formatted_rows = [[id, name, biography]]

                # Define column headers
                headers = ["ID", "Name", "Biography"]

                # Print the table using tabulate
                print(tabulate(formatted_rows, headers=headers, tablefmt="grid"))
           
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()