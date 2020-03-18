from flask import Flask, render_template, redirect, \
    url_for, request, session
from functools import wraps
import sqlite3

app = Flask(__name__)

app.secret_key = "my precious"
app.datebase = "sample.db"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    g.db = connect_db()
    cur = g.db.execute('Select * from posts')
    
    posts = []
    for row in cur.fetchall():
        post_dict
        post_dict
        posts.append(dict(title=row[0], description=row[1]))
        print(post_dict)
        
    #posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]

    g.db.close()
    return render_template("index.html", posts=posts)

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.methond == 'POST':
        if request.form['username'] != 'admin' or rquest.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_templat('login.html', error=error)

@app.route('/loggout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))

def connect_db():
    return sqlite3.connect(app.datebase)
    
if __name__ == '_main_':
    app.run(debug=True)