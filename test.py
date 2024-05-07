import mysql
import mysql.connector
db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="alessio",
            database="mydbristorante"
        )
cur = db.cursor()
cur.execute("SELECT * FROM elementomagazzino")
result = cur.fetchall()
print(result)
print((result[1][0]))