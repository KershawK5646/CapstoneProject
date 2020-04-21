from flask import g
import DAO
import MSUTIL
import sqlite3

def viewBookedRooms():
    print('Begin View booked rooms file')
    print('Connecting to database')
    sqliteConnection = DAO.connect_db()
    print('Connection established')
    print('Assigning query')
    showAllQuery = 'select * from bookedInventoryTable'
    cursor = sqliteConnection.execute(showAllQuery)
    queryResults = sqliteConnection.execute(showAllQuery)
    print(queryResults)
    print('Pulling all bookings')
    bookings= [dict(roomBookingNumber=row[0], roomNumber=row[1], 
                    roomName=row[2], bookedDate=row[3], bookedTime=row[4], 
                    attendance=row[5], purpose=row[6], 
                    bookedBy=row[7]) for row in cursor.fetchall()]
    print('Bookings pulled')
    print(bookings)
    print('END OF roomBookings.py RETURNING DATA')
    return bookings