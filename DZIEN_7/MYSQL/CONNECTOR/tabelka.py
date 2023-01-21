import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database="dbtestowa")
cursorObject = db.cursor()

tabelka = "CREATE TABLE IF NOT EXISTS student (name varchar(255), nb int);"
cursorObject.execute(tabelka)
print("tabela została utworzona...")
student_dane = "INSERT INTO student (name,nb) VALUES (%s,%s)"
val = ("Anna",4353)
cursorObject.execute(student_dane,val)
db.commit()
print(f'wstawiono rekordów: {cursorObject.rowcount}')
db.close()
