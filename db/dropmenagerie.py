import mysql.connector
from mysql.connector import Error

def drop_database_if_exists(database_name):
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
            databases = [db[0] for db in cursor.fetchall()]
            if database_name in databases:
                cursor.execute(f"DROP DATABASE {database_name}")
                print(f"The database '{database_name}' has been dropped.")
            else:
                print(f"The database '{database_name}' does not exist.")

    except Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed.")

drop_database_if_exists("menagerie")
