import mysql.connector

def fetch_female_dogs():
    connection = None
    try:

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Manar2222$",
            database="menagerie"
        )

        cursor = connection.cursor()
        query = "SELECT * FROM pet WHERE species = 'dog' AND sex = 'f';"
        cursor.execute(query)
        rows = cursor.fetchall()
        print(f"{'Name':<10} {'Owner':<10} {'Species':<10} {'Sex':<5} {'Birth':<12} {'Death':<12}")
        print("-" * 60)
        for row in rows:
            name = row[0] or "None"
            owner = row[1] or "None"
            species = row[2] or "None"
            sex = row[3] or "None"
            birth = row[4] if row[4] else "None"
            death = row[5] if row[5] else "None"
            print(f"{name:<10} {owner:<10} {species:<10} {sex:<5} {str(birth):<12} {str(death):<12}")

    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:

        if connection and connection.is_connected():
            cursor.close()
            connection.close()

fetch_female_dogs()
