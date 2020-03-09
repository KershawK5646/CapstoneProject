# inport the Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request

# create the application abject
app = Flask(__name__)

# user decorators to link the function to a url
@app.route('/')
def home():
	return "Hello, world!"	# return a string

@app.route('/welcome')
def welcome():
	return render_template("welcome.html")	# render a template

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid credentials. Please try again.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error=error)



# start the server with the 'run()' method
if __name__ == '__main__':
	app.run(debug=True)