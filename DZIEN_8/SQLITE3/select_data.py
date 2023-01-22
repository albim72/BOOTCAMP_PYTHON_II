import sqlite3
from sqlite3 import Error
from conn import create_connection

def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    
    rows = cur.fetchall()
    for row in rows:
        print(row)


def select_all_projects(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM projects")

    rows = cur.fetchall()
    for row in rows:
        print(row)
