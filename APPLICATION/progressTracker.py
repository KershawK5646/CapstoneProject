'''
progressTracker

This file pulls data from the updates table of the database for Makerspace
and helps display it on a web page.

Using bookARoom.py for reference.
'''
# Imports
import DAO

def viewGitUpdates():
    print('Begin progressTracker.py')
    print('Connecting to database')
    sqliteConnection = DAO.connect_db()
    print('Database connection established')
    print('Assigning query value')
    showAllQuery = 'select * from updates'
    print('Query assigned')
    print('Querying the database')
    cursor = sqliteConnection.execute(showAllQuery)
    print('Returning data')
    progressReport = [dict(updateNumber=row[0],updateTitle=row[1],
                           updateDescription=row[2],dateCompleted=row[3],
                           uodatedBy=row[4]) for row in cursor.fetchall()]
    #print(progressReport)
    print('Data returned')
    return(progressReport)