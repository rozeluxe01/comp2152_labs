import sqlite3
from contextlib import closing

try:
    with closing(sqlite3.connect('test.db')) as db_conn:
        db_conn.row_factory = sqlite3
        with closing(db_conn.cursor()) as cursor:
            try:
                query_1 = "SELECT * FROM demo WHERE ID > 14"
                cursor.execute(query_1)
                rows = cursor.fetchall()
                for row in rows:
                    print(row["name"])
            except:
                print(f"Error Executing Query 1")

            try:
                del_row = int(input("Enter the row ID threshold for deletion:"))
                query_2 = "DELETE FROM demo WHERE ID < ?"
                cursor.execute(query_2, (del_row, ))
                num_rows = cursor.rowcount
                print(f"{num_rows} rows affected")
                db_conn.commit()
            except:
                print(f"Error Executing Query 2")
except sqlite3.Error as e:
    print(f"Databas Connection Error")