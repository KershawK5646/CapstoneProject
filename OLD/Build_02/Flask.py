''' Build 0.2 '''
# imports
from flask import Flask, render_template, redirect, url_for, request, session
from flask import flash
from functools import wraps
import loginProgram

# Create the application object
app = Flask(__name__)

# TODO Add secret key properly
app.secret_key = "This is my secret key"
app.database = "users.db"

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


# Logout page
@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash("You've just been logged out!")
    return redirect(url_for('index'))

'''
# Show users in db
@app.route('/showusers')
@login_required
def show_users():
    g.db = connect_db()
    cur = g.db.execute('select username from users')
    users = [dict(username=row[0]) for row in cur.fetchall()]
    return render_template('index.html', users = users)

# Database connection
def connect_db():
    return sqlite3.connect(app.database)
'''
# Start the application
if __name__ == '__main__':
    app.run()