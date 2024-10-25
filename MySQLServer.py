import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        # Establish the connection to MySQL
        connection = mysql.connector.connect(
            host="localhost",  
            user="root",  
            password="Turin1945!" 
        )

        # Creating a cursor object using the connection
        cursor = connection.cursor()
        
        # SQL query to create the database, using IF NOT EXISTS to avoid errors if it exists
        create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

        # Execute the query
        cursor.execute(create_db_query)

        # Success message
        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Access denied. Please check your username and password.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: Database does not exist.")
        else:
            print(f"Error: {err}")
    finally:
        # Close cursor and connection
        if cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("Connection closed.")

# Run the function
create_database()
