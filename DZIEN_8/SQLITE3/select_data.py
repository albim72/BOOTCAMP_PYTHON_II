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

def select_task_by_priority(conn,priority):
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority = ?",(priority,))

    rows = cur.fetchall()
    for row in rows:
        print(row)

def select_taks():
    database = r"c:\sqlite\db\bazaprojektow.db"
    conn = create_connection(database)
    with conn:
        print("1. Wyświetlenie wszystkich zadań...")
        select_all_tasks(conn)
        print("2. Wyświetlenie wszystkich zadań po priorytecie...")
        select_task_by_priority(conn,1)

def select_projects():
    database = r"c:\sqlite\db\bazaprojektow.db"
    conn = create_connection(database)
    with conn:
        print("1. Wyświetlenie wszystkich projektów...")
        select_all_projects(conn)
