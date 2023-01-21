import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database="dbtestowa")
cursorObject = db.cursor()

print("Wyświetlanie danych z pomocą kaluzuli SELECT... z WHERE")
dane = "SELECT * FROM student WHERE nb>=100000;"
cursorObject.execute(dane)

print(cursorObject)
wynik = cursorObject.fetchall()

for x in wynik:
    print(x)
db.close()
