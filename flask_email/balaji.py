from flask import Flask
from flask_mail import Mail, Message

app = Flask(name)
mail= Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'nanimuvvala18@gmail.com'
app.config['MAIL_PASSWORD'] = 'qucbuddnmfpbycys'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello Sir! 2100031949 Here!', sender = 'nanimuvvala18@gmail.com', recipients =
['deepak@kluniversity.in'])
   msg.body = "Hello from Flask,ID:2100031949,M.V.N.Balaji"
   mail.send(msg)
   return "Sent"

if name== 'main':
   app.run(debug = True)
