'''
Book a room
'''
import MSUTIL

def createRoomBooking(roomBooked, bookingDate, enteredAttendance,
                                    bookingPurpose, bookedBy):
    print('Begin bookARoom.py')
    print('Stripping quotes from text.')
    roomBooked = MSUTIL.stripSingleQuotes(roomBooked)
    bookingDate = MSUTIL.stripSingleQuotes(bookingDate)
    enteredAttendance = MSUTIL.stripSingleQuotes(enteredAttendance)
    bookingPurpose = MSUTIL.stripSingleQuotes(bookingPurpose)
    bookedBy = MSUTIL.stripSingleQuotes(bookedBy)
    
    print(roomBooked)
    print(bookingDate)
    print(enteredAttendance)
    print(bookingPurpose)
    print(bookedBy)
    
    return True