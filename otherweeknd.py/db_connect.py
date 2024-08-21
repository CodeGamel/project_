import mysql.connector
from mysql.connector import Error

def connect_db():
    db_name = 'module5db'
    user = 'root'
    password = 'Steamisbetter11-'
    host = 'localhost'

    try:
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

        if conn.is_connected():
            print("Connection to MySQL database successful!")
            return conn
    
    except Error as e:
        print(f"Error: {e}")
        return None