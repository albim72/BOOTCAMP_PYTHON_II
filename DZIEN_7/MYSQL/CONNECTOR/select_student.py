import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database="dbtestowa")
cursorObject = db.cursor()

print("Wyświetlanie danych z pomocą kaluzuli SELECT...")
dane = "SELECT name, nb FROM student"
cursorObject.execute(dane)

print(cursorObject)
wynik = cursorObject.fetchall()

for x in wynik:
    print(x)
db.close()
