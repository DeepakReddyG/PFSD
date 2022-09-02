from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your_email'
app.config['MAIL_PASSWORD'] = 'your_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello Sir! 2100031817 Here!', sender = 'your_email', recipients = 
['deepak@kluniversity.in'])
   msg.body = "Hello from Flask,ID:2100031817,Deepak Reddy Gathpa"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
