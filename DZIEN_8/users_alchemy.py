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
