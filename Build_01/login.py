''' Build 0.1 '''
# imports
from flask import Flask, render_template, redirect, url_for, request, session
from flask import flash, g
from functools import wraps
import sqlite3

# Create the application object
app = Flask(__name__)

# TODO Add secret key properly
app.secret_key = "This is my secret key"
app.database = "sample.db"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

# Use decorators to link the function to a URL
# Basic / page to test.
@app.route('/')
@login_required
def home():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()] 
    return render_template('index.html', posts=posts) # Render the template

# Welcome page to greet the user
@app.route('/welcome')
def welcome():
    return render_template('welcome.html') # render a template

# Login page.
@app.route('/login', methods=['GET','POST'])
def login():
    error = None # set a value for the error.
    if request.method == 'POST': # If the user is inputting data:
        # If the data put in != admin, admin, grant access
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again' #Kick back for invalid creds.
        else:
            # If the data is correct, login session is granted
            session['logged_in'] = True
            # Give the user feedback that the login was successful
            flash('You were just logged in!')
            # redirect the user to the home page.
            return redirect(url_for('home'))
    # Return the user to the login page if bad creds entered. 
    # Display the error.
    return render_template('login.html', error=error)

# Logout page.
@app.route('/logout')
@login_required
def logout():
    # Pop the sessions login status and replace with None variable
    session.pop('logged_in', None)
    # Give the user feedback that the log out was successful
    flash('You were just logged out!')
    # Return the user to the welcome page.
    return redirect(url_for('welcome'))


# Database Access Object
def connect_db():
    return sqlite3.connect(app.database)

# Start the server with the run method
if __name__ == '__main__':
    app.run(debug=False)