'''USER OBJECT'''
class User:
    def __init__(self, userID, email, username, password, phoneNumber):
        self.userID = userID
        self.email = email
        self.username = username
        self.password = password
        self.phoneNumber = phoneNumber
        
        # Create setters
        def set_userID(self, userID):
            self.__userID = userID
            
        def set_email(self, email):
            self.__email = email
        
        def set_username(self, username):
            self.__username = username
        
        def set_password(self, password):
            self.__password = password
        
        def set_phoneNumber(self, phoneNumber):
            self.__phoneNumber = phoneNumber
        
        #Create getters
        def get_userID(self, userID):
            return self.__userID
            
        def get_email(self, email):
            return self.__email
        
        def get_username(self, username):
            return self.__username
        
        def get_password(self, password):
           return self.__password
        
        def get_phoneNumber(self, phoneNumber):
            return self.__phoneNumber
        
        def __str__(self):
            return "UserID: " + self.__userID + \
                "\nEmail: " + self.__email + \
                "\nUsername: " + self.__username + \
                "\nPassword: " + self.__password + \
                "\nPhone Number: " + self.__phoneNumber
                