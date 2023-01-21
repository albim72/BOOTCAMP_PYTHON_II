import mysql.connector

def filtr(pal):
    db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database="dbtestowa")
    cursorObject = db.cursor()

    print(f"tabela po filrowaniu po palecie: {pal}")

    query = 'SELECT idkoloru, nazwa_koloru, nazwa_palety FROM kolor WHERE nazwa_palety ="' + pal  + '"'
    cursorObject.execute(query)
    wynik = cursorObject.fetchall()
    for i,k,p in wynik:
        print(f'id: {i}, kolor: {k}, paleta: {p}')
    db.close()
