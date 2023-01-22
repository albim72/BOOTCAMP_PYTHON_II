import sqlite3
from sqlite3 import Error
from conn import create_connection

def create_table(conn,create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def cr():
    database = r"c:\sqlite\db\bazaprojektow.db"
    sql_create_projects_table = """
        CREATE TABLE IF NOT EXISTS projects (
            id integer PRIMARY KEY,
            name text NOT NULL,
            begin_date text NOT NULL,
            end_date text NOT NULL,
    );
    """
    sql_create_tasks_table = """
        CREATE TABLE IF NOT EXISTS tasks (
            id integer NOT NULL PRIMARY KEY,
            name text NOT NULL,
            priority integer NOT NULL,
            status_id integer NOT NULL,
            project_id integer NOT NULL,
            begin_date text NOT NULL,
            end_date text NOT NULL,
            FOREIGN KEY(project_id) REFERENCES projects(id)
            );
    """
