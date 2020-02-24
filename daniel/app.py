from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
	return "Hello, world!"


@app.route('/welcome')
def welcome():
	return render_template("welcome.html")


if __name__ == '__main__':
	app.run(debug=True)