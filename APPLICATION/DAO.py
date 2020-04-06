''' Build 0.2 '''
import sqlite3
from flask import Flask, g

# Define the database
db_app = Flask(__name__)
db_app.database = "makerSpace_db.db"

# Database connection
def connect_db():
    return sqlite3.connect(db_app.database)




# Start the application
if __name__ == '__main__':
    db_app.run()