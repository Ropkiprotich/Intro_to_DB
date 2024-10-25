import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Turin1945!",
    database="alx_book_store"
)

print(mydb.get_server_info())