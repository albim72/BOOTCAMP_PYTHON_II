import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database="dbtestowa")
cursorObject = db.cursor()

studenci_dane = "INSERT INTO student (name,nb) VALUES (%s,%s)"
val = [
    ("Olaf",32423),
    ("Olga",77657),
    ("Feliks",53454),
    ("Nadia",676656),
    ("Maria",452445),
    ("Jacek",675645),
]

cursorObject.executemany(studenci_dane,val)
db.commit()
print(f'wstawiono rekordów: {cursorObject.rowcount}')
db.close()
