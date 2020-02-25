''' Build 0.2 '''
import sqlite3

with sqlite3.connect("users.db") as connection:
    c = connection.cursor()
    # TODO Delete the drop table command
    #c.execute("DROP TABLE posts")
    # Create the table
    c.execute("CREATE TABLE users(user_id integer primary key ,username Text, password TEXT)")
    # Create users and dummy passwords
    c.execute('INSERT INTO users VALUES(1, "Kersahwk5646", "P@ssword1")')
    c.execute('INSERT INTO users VALUES (2,"Praterj5446", "St4rD3wV4ll3y")')
    c.execute('INSERT INTO users VALUES (3, "biglerd7304","Blu3Gr33n")')
    c.execute('INSERT INTO users VALUES(4, "user2", "P@ssword2")')