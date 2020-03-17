''' BUILD 0.2 '''
import DAO
import MSUTIL

def compareCreds(enteredName, enteredPassword):
    try:
        #Variable needed for query
        unique = "username = '"+enteredName+"'"
        # Query the database
        userPassword = pullUserPassword('*', 'users', unique)
        # Strip the returned data of quotes
        userPassword = MSUTIL.stripSingleQuotes(userPassword[0])
        #Compare password. If correct, allow. If not, deny
        if enteredPassword != userPassword:
            return False
        else:
            return True

    # Return false if username entered is not in DB
    except:
        return False


#Search database for specific fields
def pullUserPassword(selection, table, unique):
    # Connect to database
    queryObject = DAO.connect_db()
    # Create a cursor object and parse the table for usernames
    cur = queryObject.execute('SELECT '+selection + ' FROM ' + table + ' where '+ unique)
    # Store query results in a list
    # Row 2 is the password in current build
    contents = [row[3] for row in cur.fetchall()]
    
    # Return the list to be used
    return contents