from flask import Flask
import random
import string
app = Flask(__name__) 
@app.route('/')
def random_string():
	for i in range(3):
		result_str = ''.join(random.sample(string.ascii_lowercase,8)) 
		return result_str

if __name__ == '__main__':  
   app.run(debug = True)
