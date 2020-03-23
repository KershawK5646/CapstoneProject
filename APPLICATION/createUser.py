'''
Create user
'''
from flask import g
import random
import DAO
import MSUTIL
import sqlite3

'''
TODO
EMAIL VERIFICATION DOESN'T WORK (allows duplicates under same email)
Username duplicates need to be eleminated
'''


def createUserMethod(emailAddress, newUsername, Password, verifiedPassword, phoneNumber):
    MSUTIL.debugFormat()
    #Strip the entered data
    emailAddress = MSUTIL.stripSingleQuotes(emailAddress)
    newUsername = MSUTIL.stripSingleQuotes(newUsername)
    Password = MSUTIL.stripSingleQuotes(Password)
    verifiedPassword = MSUTIL.stripSingleQuotes(verifiedPassword)
    phoneNumber = MSUTIL.stripSingleQuotes(phoneNumber)

    emailExists = testEmail(emailAddress)
    print(emailAddress)
    if (emailExists==True):
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
            return True
    
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
            return False

        
        
    
        
    
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
    try:
        emailAddress = MSUTIL.stripSingleQuotes(emailAddress)
        queryObject = DAO.connect_db()
        unique = "email = '"+emailAddress+"'"
        databaseQuery = 'SELECT * FROM users where '+unique
        cur = queryObject.execute(databaseQuery)
        contents = [row[1] for row in cur.fetchall()]
        contents = MSUTIL.stripSingleQuotes(contents[0])
        if emailAddress == contents:
            return True
        else:
            return False
    except:
        return False