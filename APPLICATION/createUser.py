'''
Create User
'''
from flask import g
import random
import DAO
import MSUTIL
import sqlite3
#import userObject

def createUserMethod(emailAddress, newUsername, Password, verifiedPassword, phoneNumber):
    MSUTIL.debugFormat()
    
    print("Begin createUserMethod().")
    #Strip the entered data
    print("Stripping Data of misc characters")
    emailAddress = MSUTIL.stripSingleQuotes(emailAddress)
    newUsername = MSUTIL.stripSingleQuotes(newUsername)
    Password = MSUTIL.stripSingleQuotes(Password)
    verifiedPassword = MSUTIL.stripSingleQuotes(verifiedPassword)
    phoneNumber = MSUTIL.stripSingleQuotes(phoneNumber)
    print("Characters stripped")
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
            print("userID: ",userID)
            print("Testing User ID")
            userIDExists = testUserID(userID)
            print("UserID Test complete. UserID is unique.")
            print("Entering user information to the Database.")
        try:
            print("Connectiong to db.")
            sqliteConnection = DAO.connect_db()
            cursor = sqliteConnection.cursor()
            print("Connection Established. Cursor Created.")
            #print("Creating new user Object")
            #newUser = userObject.UserObject(userID, emailAddress, newUsername, Password, phoneNumber)
            print("User object created")
            print("Begin insert data command.")
            
            sqlite_insert_with_param = '''INSERT INTO userObjectTable 
            (user_id, email, username, password, phoneNumber)
            VALUES
            (?,?,?,?,?);'''
            data_tuple = (userID, emailAddress, newUsername, Password, phoneNumber)
            cursor.execute(sqlite_insert_with_param, data_tuple)
            print("Data written to DB successfully.")
            sqliteConnection.commit()
            print("Database Saved")
            cursor.close()
            print("Connection to DB closed.")
            print("Finish createUserMethod().")
            return True
    
        except sqlite3.Error as error:
            print("Failed to insert data into sqlite table", error)
            print("Finish createUserMethod().")
            return False
        
        
        
# Test to see if userID is in use
def testUserID(userID):
    print("Begin testUserID().")
    # Search db for existing User ID
    # Connect to database
    print("Connecting to db.")
    userIDTester = DAO.connect_db()
    print("Connection Established")
    selectAllQuery = 'SELECT * FROM userObjectTable'
    cur = userIDTester.execute(selectAllQuery)
    print("Query Generated")
    print("Searching db for UserID")
    records = cur.fetchall()
    print("Records Returned")
    print("Verifying UserID is unique.")
    for row in records:
        if (row[1]==userID):
            print("UserID Exists. Returning True")
            userIDInUse = True
        else:
            print("UserID is unique. Returning False")
            userIDInUse = False
    print("Returning previous value.")
    return userIDInUse





# Test to see if email is in use
def testEmail(emailAddress):
    print("Begenning testEmail().")
    try:
        print("Strip email of special characters.")
        emailAddress = MSUTIL.stripSingleQuotes(emailAddress)
        print("Connection to database.")
        queryObject = DAO.connect_db()
        print("Connection Established")
        print("Generating query")
        unique = "email = '"+emailAddress+"'"
        databaseQuery = 'SELECT * FROM userObjectTable where '+unique
        print("Passing Query to DB")
        cur = queryObject.execute(databaseQuery)
        contents = [row[1] for row in cur.fetchall()]
        contents = MSUTIL.stripSingleQuotes(contents[0])
        print("Results returned")
        print("Testing email to verify unique")
        if emailAddress == contents:
            print("Email Exists. Returning True")
            return True
        else:
            print("Email is unique. Returning False")
            return False
    except:
        print("Unidentified Error in testEmail(). Returning False")
        return False