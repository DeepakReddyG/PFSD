from flask import Flask
from flask_mail import Mail, Message
app = Flask(__name__)
mail = Mail(app) 

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'deepakreddygathpa@gmail.com'
app.config['MAIL_PASSWORD'] = 'sboctpazvpuhmoix' 
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True 
mail = Mail(app)
@app.route("/")
def index():
	msg = Message('Hello :) From Flask (generated By Deepak)', sender = 
'deepakreddygathpa@gmail.com', recipients = ['gongati.sujithreddy2004@gmail.com']) 
	msg.body = "Hello there :),I have used your email to test the working of flask_mail!"
	mail.send(msg)
	return "message sent successfully :) "
if __name__ == '__main__':
	app.run(debug=True)
