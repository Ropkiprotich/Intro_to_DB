import mysql.connector
from mysql.connector import errorcode

def create_database():
    connection = None  # Initialize the connection variable
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host="localhost",  # Replace with your host if different
            user="root",       # Replace with your MySQL username
            password="your_password"  # Replace with your MySQL password
        )
        cursor = connection.cursor()

        # Attempt to create the database
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        # Success message
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: The database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Ensure connection is closed only if it was established
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
