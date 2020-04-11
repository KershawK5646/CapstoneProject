'''BOOKED ROOM OBJECT'''
class bookedRoom:
    def __init__(self, dateBooked, timeBooked, bookedBy, attendence, Purpose):
        self.dateBooked = dateBooked
        self.timeBooked = timeBooked
        self.bookedBy = bookedBy
        self.attendence = attendence
        self.Purpose = Purpose
        
        # Create setters
        def set_dateBooked(self, dateBooked):
            self.__dateBooked = dateBooked
            
        def set_timeBooked(self, timeBooked):
            self.__timeBooked = timeBooked
        
        def set_bookedBy(self, bookedBy):
            self.__bookedBy = bookedBy
        
        def set_attendence(self, attendence):
            self.__attendence = attendence
        
        def set_Purpose(self, Purpose):
            self.__Purpose = Purpose
        
        #Create getters
        def get_dateBooked(self, dateBooked):
            return self.__dateBooked
            
        def get_timeBooked(self, timeBooked):
            return self.__timeBooked
        
        def get_bookedBy(self, bookedBy):
            return self.__bookedBy
        
        def get_attendence(self, attendence):
           return self.__attendence
        
        def get_Purpose(self, Purpose):
            return self.__Purpose
        
        def __str__(self):
            return "DateBooked: " + self.__dateBooked + \
                "\nTimeBooked: " + self.__timeBooked + \
                "\nBookedBy: " + self.__bookedBy + \
                "\nAttendence: " + self.__attendence + \
                "\nPurpose: " + self.__Purpose