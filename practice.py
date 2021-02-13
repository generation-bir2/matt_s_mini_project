
import mysql.connector
con = mysql.connector.connect(
host="localhost",
user="root",
password="password",
database="test"
)

try:

    with con.cursor() as cur:
        

        cur.execute('SELECT curdate();')

        rows = cur.fetchall()
        

        for row in rows:
            print(f'{row[0]}')

finally:

    con.close()