from flask import *
app = Flask(__name__)
@app.route('/login', methods=['POST'])
def login():
	uname = form.request['uname']
	passwd = form.request['pass']	
	if uname=='Deepak' and passwd=='12345':
		return "login successful, you are logged in as %s"%uname
	else:
		return "login unsuccessful"
if __name__ == '__main__':
	app.run(debug=True)
	
