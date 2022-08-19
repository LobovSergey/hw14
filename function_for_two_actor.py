import sqlite3


def two_actor():
    with sqlite3.connect('netflix.db') as connection:
        cursor = connection.cursor()
        query = """
                   SELECT COUNT(*), `cast`
                   FROM netflix
                   GROUP BY 'cast'                 
                   """
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
