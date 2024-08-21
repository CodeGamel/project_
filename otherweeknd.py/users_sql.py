import mysql.connector
from mysql.connector import Error
from tabulate import tabulate
from db_connect import connect_db
def add_user():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input("Enter your name:   ").title()
            library_id = input("Enter your library ID:  ")

            new_user = (name,library_id)

            query = "INSERT INTO users (name, library_id) VALUES (%s, %s)"

            cursor.execute(query, new_user)
            conn.commit()
            print(f'New user: {name} added succesfully! Welcome!!')
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
if __name__ == "__main__":
    add_user()


def display_users():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            # Selecting all books
            fetch_query = "SELECT * FROM users;"
            cursor.execute(fetch_query)
           
            rows = cursor.fetchall()

            # Get column names from cursor description
            column_names = [desc[0] for desc in cursor.description]

            # Format the rows for tabulate
            formatted_rows = [list(row) for row in rows]

            # Print the table using tabulate
            print(tabulate(formatted_rows, headers=column_names, tablefmt="grid"))

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn:
                cursor.close()
                conn.close()
    
def view_user_details():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()
            user_id = input("Enter the User ID to view details: ")

            query = "SELECT * FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))

            # Fetch the result
            user_details = cursor.fetchone()

            if user_details:
                print("\nUser Details:")
                print(f"Library_ID: {user_details[0]}")
                print(f"Name: {user_details[1]}")
                print(f"Email: {user_details[2]}")
            else:
                print("No user found with the provided ID.")

        except Error as e:
            print(f"Error: {e}")
