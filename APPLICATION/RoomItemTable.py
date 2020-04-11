'''ROOM ITEM TABLE OBJECT'''
class RoomItemTable:
    def __init__(self, roomNumber, roomName, canHold):
        self.roomNumber = roomNumber
        self.roomName = roomName
        self.canHold = canHold
        
        # Create setters
        def set_roomNumber(self, roomNumber):
            self.__roomNumber = roomNumber
            
        def set_roomName(self, roomName):
            self.__roomName = roomName
        
        def set_canHold(self, canHold):
            self.__canHold = canHold
        
        #Create getters
        def get_roomNumber(self, roomNumber):
            return self.__roomNumber
            
        def get_roomName(self, roomName):
            return self.__roomName
        
        def get_canHold(self, canHold):
            return self.__canHold
        
        def __str__(self):
            return "RoomNumber: " + self.__roomNumber + \
                "\nRoomName: " + self.__roomName + \
                "\nCanHold: " + self.__canHold