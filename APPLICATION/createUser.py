'''
Create user
'''
from flask import g
import random
import DAO
import MSUTIL
import sqlite3


def createUserMethod(emailAddress, newUsername, Password, verifiedPassword, phoneNumber):
    MSUTIL.debugFormat()
    #Strip the entered data
    emailAddress = MSUTIL.stripSingleQuotes(emailAddress)
    newUsername = MSUTIL.stripSingleQuotes(newUsername)
    Password = MSUTIL.stripSingleQuotes(Password)
    verifiedPassword = MSUTIL.stripSingleQuotes(verifiedPassword)
    phoneNumber = MSUTIL.stripSingleQuotes(phoneNumber)

    testEmail(emailAddress)

    if (testEmail==False):
        return False
    
    else:
        userIDExists = True
        while userIDExists == True:
            # Create random number for user ID
            # Test the number for use
            userID=random.randint(0,9999)
            userIDExists = testUserID(userID)
        
        try:
            sqliteConnection = DAO.connect_db()
            cursor = sqliteConnection.cursor()
            print("Successfully Connected to SQLite")
        
            sqlite_insert_with_param = '''INSERT INTO users 
            (user_id, email, username, password, phoneNumber)
            VALUES
            (?,?,?,?,?);'''
            
            data_tuple = (userID, emailAddress, newUsername, Password, phoneNumber)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            
            sqliteConnection.commit()
            cursor.close()
    
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)

        
        return True
    
        
    
# Test to see if userID is in use
def testUserID(userID):
    MSUTIL.debugFormat()
    # Search db for existing User ID
    # Connect to database
    userIDTester = DAO.connect_db()
    selectAllQuery = 'SELECT * FROM users'
    cur = userIDTester.execute(selectAllQuery)
    records = cur.fetchall()
    for row in records:
        if (row[1]==userID):
            userIDInUse = True
        else:
            userIDInUse = False
    MSUTIL.debugFormat()
    return userIDInUse

# Test to see if email is in use
def testEmail(emailAddress):
    MSUTIL.debugFormat()
    # Search db for existing User Email
    # Connect to database
    emailTester = DAO.connect_db()
    selectAllQuery = 'SELECT * FROM users'
    cur = emailTester.execute(selectAllQuery)
    records = cur.fetchall()
    for row in records:
        if (row[1]==emailAddress):
            userEmailInUse = True
        else:
            userEmailInUse = False

    MSUTIL.debugFormat()
    return userEmailInUse