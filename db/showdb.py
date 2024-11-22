import mysql.connector
from mysql.connector import Error

def show_databases():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Manar2222$"
        )
        if connection.is_connected():
            print("Connected to MySQL server")

            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")
            print("Databases on the server:")
            for db in cursor:
                print(db[0])

    except Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")

show_databases()
