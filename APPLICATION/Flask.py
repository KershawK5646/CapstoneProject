''' Build 0.2 '''
# imports
from flask import Flask, render_template, redirect, url_for, request, session
from flask import flash
from functools import wraps
import createUser
import loginProgram
import viewBookings
import progressTracker

# Create the application object
app = Flask(__name__)

# TODO Add secret key properly
app.secret_key = "This is my secret key"
app.database = "makerSpace_db.db"

# Logged in function required
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to log in first.')
            return redirect(url_for('login'))
    return wrap


''' 
PAGES
'''
# TODO: This is the main page
@app.route('/home')
@login_required
def index():
    progressReport = progressTracker.viewGitUpdates()
    return render_template('index.html', progressReport=progressReport)

@app.route('/')
def slash():
    return redirect(url_for('index'))



# Login page
@app.route('/login', methods = ['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        enteredName = request.form['username']
        enteredPassword = request.form['password']
        if loginProgram.compareCreds(enteredName, enteredPassword) == False:
            error = 'Invalid credentials. Please try again'
             
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('index'))
        
    return render_template('login.html', error = error)    





# Create user page
@app.route('/newuser', methods = ['GET','POST'])
def newUser():
    error = None
    if request.method == 'POST':
        
        # Collect information needed for new user.
        emailAddress = request.form['emailAddress']
        newUsername = request.form['newUsername']
        password = request.form['password']
        verifiedPassword = request.form['verifiedPassword']
        phoneNumber = request.form['phoneNumber']

        # Pass information to create user program.
        if createUser.createUserMethod(emailAddress, newUsername, password, verifiedPassword, phoneNumber) == False:
            error = 'Looks like you already have an account. Please log in'
        
        else:
            session['logged_in'] = True
            flash('Your account has been created!')
            return redirect(url_for('welcome'))
        
    return render_template('newuser.html', error = error)   
    #return redirect(url_for('error'))
    

# About page
@app.route('/about')
def about():
    return render_template('about.html')
    
    
# Logout page
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash("You've just been logged out!")
    return redirect(url_for('index'))

# Welcome page
@app.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html')


# Error page
@app.route('/error')
def error():
     return render_template('error.html')


# Contact Page
@app.route('/contact')
def contact():
    return render_template('contact.html')
    

# View booked rooms
@app.route('/view_booked_rooms')
@login_required
def viewBookedRooms():
    bookings = viewBookings.viewBookedRooms()    
    return render_template('view_booked_rooms.html', bookings = bookings)


# View booked rooms
@app.route('/view_booked_inventory')
@login_required
def viewBookedInventory():
    bookedItems = viewBookings.viewBookedInventory()
    return render_template('view_booked_inventory.html', bookedItems = bookedItems)

# Book a room page
@app.route('/bookARoom', methods = ['GET','POST'])
@login_required
def bookARoom():
    print('BOOK A ROOM PAGE')
    flash('Book a room!')
    listStatus = [('woodworking lab a','Woodworking Lab A'),
                  ('robotics lab a','Robotics Lab A'),
                  ('3d printer room','3D Printer Room'),
                  ('kitchen lab','Kitchen Lab'),
                  ('woodworking lab b','Woodworking Lab B'),
                  ('metalworking lab a','Metalworking Lab A'),
                  ('metalworking lab b','Metalworking Lab B')]
    default = 'woodworking lab a'
    
    error = None
    if request.method == 'POST':
        print('ASSIGNING VARIABLES FROM WEBFORM')
        # Assign variables
        roomBooked = request.form['roomBooked']
        print('roomBooked Assigned')
        bookingDate = request.form['bookingDate']
        print('bookingDate Assigned')
        enteredAttendance = request.form['enteredAttendance']
        print('enteredAttendance Assigned')
        bookingPurpose = request.form['bookingPurpose']
        print('bookingPurpose Assigned')
        bookedBy = request.form['bookedBy']
        print('bookedBy Assigned')
        print('ALL VARIABLES ASSIGNED')
        if bookARoom.createRoomBooking(roomBooked, bookingDate, enteredAttendance, bookingPurpose, bookedBy) == False:
            error = 'Looks like there is a booking for that room and time. Please reschedule'
        else:
            flash('Reservation Booked!')
            return redirect(url_for('viewBookedRooms'))
    
    return render_template('bookARoom.html', listStatus, default, error=error)


# Dev nav page
@app.route('/dev')
def devNav():
    return render_template('dev.html')

# Start the application
if __name__ == '__main__':
    app.run()