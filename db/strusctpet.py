import mysql.connector
from mysql.connector import Error

def show_table_structure():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Manar2222$",
            database="menagerie"
        )
        if connection.is_connected():
            print("Connected to MySQL server")

            cursor = connection.cursor()
            cursor.execute("DESCRIBE pet")
            print("Table structure of 'pet' table:")
            for row in cursor.fetchall():
                print(
                    f"Field: {row[0]}, Type: {row[1]}, Null: {row[2]}, Key: {row[3]}, "
                    f"Default: {row[4]}, Extra: {row[5]}")

    except Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")

show_table_structure()
