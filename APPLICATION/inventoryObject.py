'''INVENTORY OBJECT'''
class Inventory:
    def __init__(self, itemNumber, itemName):
        self.itemNumber = itemNumber
        self.itemName = itemName
        
        # Create setters
        def set_itemNumber(self, itemNumber):
            self.__itemNumber = itemNumber
        
        def set_itemName(self, itemName):
            self.__itemName = itemName
        
        # Create getters
        def get_itemNumber(self, itemNumber):
            return self.__itemNumber
        
        def get_itemName(self, itemName):
            return self.__itemName
        
        def __str__(self):
            return "Item Number: " + self.__itemNumber + \
                "\nItem Name: " + self.__itemName
                