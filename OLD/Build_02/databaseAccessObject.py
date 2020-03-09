''' Build 0.2 '''
import sqlite3
from flask import Flask, g

# Define the database
app = Flask(__name__)
app.database = "users.db"

#Search database for specific fields
def pullUserPassword(selection, table, unique):
    
    # TODO DELETE DEBUG PRINTS
    #print('DAO.py start')
    
    # Connect to database
    g.db = connect_db()
    # Create a cursor object and parse the table for usernames
    cur = g.db.execute('SELECT '+selection + ' FROM ' + table + ' where '+ unique)
    # Store query results in a list
    # Row 2 is the password in current build
    contents = [row[2] for row in cur.fetchall()]
    
    # Return the list to be used
    return contents

# Database connection
def connect_db():
    return sqlite3.connect(app.database)

