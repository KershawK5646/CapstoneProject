import sqlite3

with sqlite3.connect("Inventory.db") as connection:
    c = connection.cursor()
    # TODO Delete the drop table command
    #c.execute("DROP TABLE users")
    # Create the table
    c.execute("CREATE TABLE users(Date Booked, Time Booked, Booked by, Equipment, Room Number)")
    # Create users and dummy passwords
    #c.execute('INSERT INTO users VALUES(1, )')
    #c.execute('INSERT INTO users VALUES (2, )')
    #c.execute('INSERT INTO users VALUES (3,)')
    #c.execute('INSERT INTO users VALUES(4, )')