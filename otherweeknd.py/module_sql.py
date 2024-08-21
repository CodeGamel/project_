import mysql.connector
from mysql.connector import Error

db_name = 'module5db'
user = 'root'
password = 'Steamisbetter11-'
host = 'localhost'

try:
    conn = mysql.connector.connect(
        database = db_name,
        user = user,
        password = password,
        host = host,
        )

    if conn.is_connected():
        print ("Connection to MySQL database successful!")
    
    cursor = conn.cursor()
    
    query = 'SELECT * FROM users;'

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

except Error as e:
    print(f"Error: {e}")

finally:
    if conn and conn.is_connected():
        cursor.close()
        conn.close()
        print("Connection successfully closed!")