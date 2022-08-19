from flask import *
import random
import string
app = Flask(__name__) 
@app.route('/')
def random_string():
	numb = request.form['numb'] 
	result_str = ''.join(random.sample(string.ascii_lowercase,int(numb))) 
	return result_str

if __name__ == '__main__':  
   app.run(debug = True)
