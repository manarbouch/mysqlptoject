import mysql.connector

def fetch_name_and_birth():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Manar2222$    ",
            database="menagerie"
        )
        cursor = connection.cursor()
        query = "SELECT name, birth FROM pet;"
        cursor.execute(query)
        rows = cursor.fetchall()

        print(f"{'Name':<10} {'Birth':<12}")
        print("-" * 25)
        for row in rows:
            name = row[0] or "None"
            birth = row[1] if row[1] else "None"
            print(f"{name:<10} {str(birth):<12}")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

fetch_name_and_birth()
