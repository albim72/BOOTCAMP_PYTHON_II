import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData,ForeignKey
from sqlalchemy import inspect
from sqlalchemy.sql import text


print(sqlalchemy.__version__)
