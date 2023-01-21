import mysql.connector

def dodawanie(nk,np):
    db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database="dbtestowa")
    cursorObject = db.cursor()

    print("dodawanie rekordu do tabeli kolor...")
    dodaj = "INSERT INTO kolor(nazwa_koloru,nazwa_palety) VALUES(%s,%s);"
    val = (nk,np)
    cursorObject.execute(dodaj,val)
    db.commit()
    print("dodano nowy kolor...")
    db.close()
