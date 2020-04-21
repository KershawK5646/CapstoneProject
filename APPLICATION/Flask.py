''' Build 0.2 '''
# imports
from flask import Flask, render_template, redirect, url_for, request, session
from flask import flash
from functools import wraps
import createUser
import loginProgram
import roomBookings

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
@app.route('/')
@login_required
def index():
    return render_template('index.html')





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
            return redirect(url_for('index'))
        
    return render_template('newuser.html', error = error)   
    #return redirect(url_for('error'))
    
    
    
    
    
# Logout page
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash("You've just been logged out!")
    return redirect(url_for('index'))




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
    bookings = roomBookings.viewBookedRooms()
    
    return render_template('view_booked_rooms.html', bookings = bookings)


# Book a room page
@app.route('/bookARoom')
@login_required
def bookARoom():
    flash('Book a room!')
    return render_template('bookARoom.html')

# Start the application
if __name__ == '__main__':
    app.run()