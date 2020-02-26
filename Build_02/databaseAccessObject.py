''' Build 0.2 '''
import sqlite3
from flask import Flask, g

# Define the database
app = Flask(__name__)
app.database = "users.db"

#Search database for specific fields
def searchdb(table, column):
    print('DAO.py start')
    g.db = connect_db()
    cur = g.db.execute('select '+column + ' from ' + table)
    contents = [dict(username=row[0]) for row in cur.fetchall()]
    return contents
    print(contents)
    print('DAO.py finished')

# Database connection
def connect_db():
    return sqlite3.connect(app.database)

