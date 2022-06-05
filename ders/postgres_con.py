import psycopg2


def postgres_connection():
    connection = psycopg2.connect(
        user="postgres",
        password="123",
        host="127.0.0.1",
        port="5432",
        database="northwind"
    )

    cursor = connection.cursor()
    #cursor.execute("SELECT * FROM categories")

    #print(cursor.fetchall())

    cursor.execute("INSERT INTO categories values (1000, 'a', 'b', 'avb')")
    connection.commit()

    print("ÇAlıştı")


postgres_connection()