from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail= Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'premcharanpremcharan335@gmail.com'
app.config['MAIL_PASSWORD'] = 'wxwxmqsfyklajrji'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('2100030857', sender = 'premcharanpremcharan335@gmail.com', 
recipients = ['deepak@kluniversity.in'])
   msg.body = "2100032221 done with sending email through flask! "
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)
