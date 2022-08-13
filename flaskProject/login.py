from flask import *
app = Flask(__name__)
@app.route('/l', methods=['POST'])
def login():
    uname = request.form['uname']
    passwrd = request.form['pass']
    if uname == "deepak" and passwrd == "123":
        return "<h1><center>Welcome %s </center><h1>" % uname
    else:
        return "Wrong Username and password"
if __name__ == '__main__':
    app.run(debug=True)
