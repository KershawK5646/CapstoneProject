''' BUILD 0.2 '''
import databaseAccessObject

def compareCreds(enteredName, enteredPassword):
    print(enteredName)
    print(enteredPassword)
    
    allUsers = databaseAccessObject.searchdb('users','username')
    
    print(allUsers)
    
    if enteredName != 'admin' or enteredPassword != 'admin':
        return False
    else:
        return True
   
    
'''
TODO:
    Pull data from DAO into a list
    Compare pulled data to entered username and PW
    return pass or fail state based on creds
    
    Salt and hash user info
    
    
    Thoughts:
        Current DAO is not accessing db properly due to app names being the same?
        
'''