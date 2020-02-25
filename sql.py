import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    # TODO Delete the drop table command
    #c.execute("DROP TABLE posts")
    c.execute("CREATE TABLE posts(title Text, description TEXT)")
    c.execute('INSERT INTO posts VALUES("Good", "I\'m, good.")')
    c.execute('INSERT INTO posts VALUES("Well", "I\'m, well.")')
