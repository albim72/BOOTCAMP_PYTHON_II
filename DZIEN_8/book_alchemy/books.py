import mysql.connector
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/bookstore',echo=True)

#metadefinicja i tworzenie tabeli
Base = declarative_base()

class Books(Base):

    __tablename__ = 'books'

    bookid = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    tytul = sqlalchemy.Column(sqlalchemy.String(length=50))
    autor = sqlalchemy.Column(sqlalchemy.String(length=50))
    oprawa = sqlalchemy.Column(sqlalchemy.String(length=50))
    lstron = sqlalchemy.Column(sqlalchemy.Integer)
    cena = sqlalchemy.Column(sqlalchemy.Float)

    def __repr__(self):
        return f"<BOOKS(tytuł = {self.tytul}, autor = {self.autor}, oprawa = {self.oprawa}," \
               f" liczba stron: {self.lstron}, cena książki: {self.cena} zł)>"

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

b1 = Books(tytul='Wiedźmin',autor='Andrzej Sapkowski',oprawa='twarda',lstron=310,cena=36.80)
session.add(b1)

b2 = Books(tytul='Hobbit',autor='J.R.R. Tolkien',oprawa='twarda',lstron=288,cena=35.5)
session.add(b2)

b3 = Books(tytul='Morderstwo w Orient Ekspressie',autor='Agatha Christie',oprawa='twarda',lstron=320,cena=41)
session.add(b3)

session.commit()

for s in session.query(Books).all():
    print(f"Książka:{s.tytul}, autor: {s.autor}")
