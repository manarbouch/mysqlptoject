import mysql.connector
from mysql.connector import Error

def fetch_name_and_birth_month():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Manar2222$',
            database='menagerie'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            query = """
            SELECT name, birth, MONTH(birth) AS birth_month 
            FROM pet;
            """
            cursor.execute(query)
            results = cursor.fetchall()
            print(f"{'Name':<10} {'Birth':<15} {'Month(Birth)':<12}")
            print("-" * 40)
            for row in results:
                name = row[0]
                birth = row[1] if row[1] else "NULL"
                birth_month = row[2] if row[2] else "NULL"
                print(f"{name:<10} {str(birth):<15} {birth_month:<12}")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

fetch_name_and_birth_month()
