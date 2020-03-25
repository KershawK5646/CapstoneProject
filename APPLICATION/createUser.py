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
    print("Stripping Data of misc characters")
    emailAddress = MSUTIL.stripSingleQuotes(emailAddress)
    newUsername = MSUTIL.stripSingleQuotes(newUsername)
    Password = MSUTIL.stripSingleQuotes(Password)
    verifiedPassword = MSUTIL.stripSingleQuotes(verifiedPassword)
    phoneNumber = MSUTIL.stripSingleQuotes(phoneNumber)
    print("Characters stripped")
    MSUTIL.debugFormat()
    print("Testing Email")
    emailExists = testEmail(emailAddress)
    print("Email Test Complete")
    print("Entered Email Address:")
    print(emailAddress)
    if (emailExists==True):
        return False
    
    print("Section 2 of User Creation:")
    else:
        print("Creating new User ID")
        userIDExists = True
        print("While loop to test userID")
        while userIDExists == True:
            # Create random number for user ID
            # Test the number for use
            print("Generating userID")
            userID=random.randint(0,9999)
            print("userID: "+userID+)
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
        print("Unidentified Error in testEmail()")
        return False