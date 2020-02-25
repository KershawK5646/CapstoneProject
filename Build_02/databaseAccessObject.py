''' Build 0.2 '''
import sqlite3
from flask import Flask, g

# Define the database
app = Flask(__name__)
app.database = "users.db"

#Search database for specific fields
def searchdb(table, column):
    g.db = connect_db()
    cur = g.db.execute('select '+column + ' from ' + table)
    contents = [dict(username=row[0]) for row in cur.fetchall()]
    print (contents)

# Database connection
def connect_db():
    return sqlite3.connect(app.database)

