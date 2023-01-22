import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy import inspect
from sqlalchemy.sql import text


print(sqlalchemy.__version__)

metadata = MetaData()
books = Table('books_best',metadata,
              Column('id',Integer,primary_key=True),
              Column('tytul',String(length=50)),
              Column('autor',String(length=50)),
              )

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/bookstore',echo=True)
s = sqlalchemy.inspect(engine).has_table("books_best")
metadata.create_all(engine)
print(s)

inspector = inspect(engine)
k = inspector.get_columns('books_best')
print(k)

with engine.connect() as conn:
    data = (
        {
            "tytul":"Hobbit",
            "autor":"J.R.R. Tolkien"
        },
        {
            "tytul": "Wiedźmin",
            "autor": "Andrzej Sapkowski"
        }
    )
    statement = text("""
        INSERT INTO books_best(tytul,autor) VALUES(:tytul,:autor)
    """)

    for line in data:
        conn.execute(statement,**line)

with engine.connect() as conn:
    r = conn.execute('SELECT * FROM books_best')
    for row in r:
        print(row)
