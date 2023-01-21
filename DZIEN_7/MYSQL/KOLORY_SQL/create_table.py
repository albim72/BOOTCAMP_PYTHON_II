import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port=3306,database="dbtestowa")
cursorObject = db.cursor()

tabelka = """
    CREATE TABLE IF NOT EXISTS kolor (
  idkoloru INT NOT NULL AUTO_INCREMENT,
  nazwa_koloru VARCHAR(45) NOT NULL,
  nazwa_palety VARCHAR(45) NOT NULL,
  PRIMARY KEY (idkoloru));
"""
cursorObject.execute(tabelka)
print("tabela została utworzona...")

db.close()
