from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
app = Flask(__name__)
@app.route("/")	
def hello():
	return "Hello,World!"
@app.route("/htmlpage")
def index():
	return render_template('hello.html')

@app.route("/login")
def login():
	uname = request.form['uname']
	passwrd = request.f

@app.route('/user/<name>')
def hello_user(name): 
	if name == 'admin': 
		return redirect(url_for('hello_admin'))
	else:
		return redirect(url_for('hello_guest', guest = name))
@app.route('/admin')
def hello_admin():
	return 'Hello Amdin' 

@app.route('/guest/<guest>')
def hello_guest(guest):
	return 'Hello %s as aguest' % guest

if __name__ == "__main__":
	app.run()
