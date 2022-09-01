from flask import *
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('base.html')
@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug = True)
