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
	msg = Message('Congrats, You won $50000!', sender='deepakreddygathpa@gmail.com', 
recipients = ['gongati.sujithreddy2004@gmail.com'])
	msg.body = "Congrats on winning 50000 usd, we would also love to gift you a ferari! :)"
	mail.send(msg)
	return 'message sent successfully to sujith'
if __name__ == '__main__':
	app.run(debug = True) 
