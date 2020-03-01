''' BUILD 0.2 '''
import databaseAccessObject

def compareCreds(enteredName, enteredPassword):
    # TODO DELETE DEBUG PRINTS
    '''
    print('==========DEBUG==========')
    print('==========LOGINPROGRAM.PY==========')
    print('Entered username:')
    print(enteredName)
    print('Entered Password')
    print(enteredPassword)
    '''
    try:
        #Variable needed for query
        unique = "username = '"+enteredName+"'"
        # Query the database
        userPassword = databaseAccessObject.pullUserPassword('*', 'users', unique)
        # Strip the returned data of quotes
        userPassword = userPassword[0].strip("'")
        #Compare password. If correct, allow. If not, deny
        if enteredPassword != userPassword:
            return False
        else:
            return True

    # Return false if username entered is not in DB
    except:
        return False
    print('==========END==========') 
