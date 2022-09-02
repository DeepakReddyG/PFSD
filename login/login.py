from flask import *
app = Flask(__name__)

@app.route('/')
def Index():
    name = 'KL University - CSE [Honors] - Y21 - PFSD - S17'
    return render_template('index.html', data = name)

@app.route('/contact')
def Contact():
    return render_template('contact.html')

@app.route('/about')
def About():
    return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)
