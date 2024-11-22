import mysql.connector

def count_pets_per_owner():
    connection = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Manar2222$",
            database="menagerie"
        )

        cursor = connection.cursor()
        query = "SELECT owner, COUNT(*) AS pet_count FROM pet GROUP BY owner;"
        cursor.execute(query)
        rows = cursor.fetchall()
        print(f"{'Owner':<10} {'Number of Pets':<15}")
        print("-" * 30)
        for row in rows:
            owner = row[0] or "None"
            pet_count = row[1]
            print(f"{owner:<10} {pet_count:<15}")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:

        if connection and connection.is_connected():
            cursor.close()
            connection.close()


count_pets_per_owner()
