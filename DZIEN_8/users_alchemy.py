import mysql.connector
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbtestowa',echo=True)

#metadefinicja i tworzenie tabeli
Base = declarative_base()

class User(Base):

    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key = True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f"<USER(name = {self.name}, fullname = {self.fullname}, nickname = {self.nickname})>"

Base.metadata.create_all(engine)
#Tworzenie sesji

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

#dodawanie użytkownika do tabeli users

p_user = User(name='Marcin', fullname='Marcin Albiniak', nickname = 'albim')
session.add(p_user)
d_user = User(name='Olga', fullname='Olga Nowak', nickname = 'olla')
session.add(d_user)
session.commit()

print("________ wyświetl rekordy___________")
for s in session.query(User).all():
    print(s.fullname)

print("________ wyświetl filtrowane rekordy___________")
for s in session.query(User).filter(User.name == "Olga"):
    print(s.fullname)


