import sqlite3
from sqlite3 import Error
from conn import create_connection
from create_tables import cr
from insert_data import insert
from select_data import select_taks, select_projects


if __name__ == '__main__':
    #create_connection(r"c:\sqlite\db\bazaprojektow.db")
    #cr()
    insert()
    select_taks()
    print("__________________")
    select_projects()
