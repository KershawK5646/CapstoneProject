'''
Login Page
'''
# imports
from flask import Flask, render_template

# Create the application object
app = Flask(__name__)

# Use decorators to link the function to a URL
@app.route('/')
def home():
    return "Hello, world!" # Returns a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html') # render a template

# Start the server with the run method
if __name__ == '__main__':
    app.run()