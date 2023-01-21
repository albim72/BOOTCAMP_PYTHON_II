import mysql.connector

def pokaz():
    db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database="dbtestowa")
    cursorObject = db.cursor()

    print("tabela po aktualizacji")

    query = "SELECT idkoloru, nazwa_koloru, nazwa_palety FROM kolor;"
    cursorObject.execute(query)
    wynik = cursorObject.fetchall()
    for i,k,p in wynik:
        print(f'id: {i}, kolor: {k}, paleta: {p}')
    db.close()
