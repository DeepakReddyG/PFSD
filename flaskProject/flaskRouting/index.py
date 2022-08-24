from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
	return "Home Page"
@app.route("/about")
def about():
	return "About page"
@app.route("/more")
def more():
	return "More page"
@app.route("/Name/<name>")
def name(name):
	return "Thank you dear "+name;
@app.route('/Age/<int:age>')
def Age(age):
	return "You are %d years old"%age;
def explore():
	return "You are now in explore page"

app.add_url_rule("/Explore","Explore",explore)

if __name__ == "__main__":
	app.run(debug = True)
