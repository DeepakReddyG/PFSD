from flask import *
from sqlalchemy import *
engine = create_engine('sqlite:///myTable.db',echo = True)
myData = Table(
        'myData', meta,
        Column('id', Integer,primary_key = True),
        Column('name',String),
        Column('father_name',String),
        Column('mother_name',String)
)
meta.create_all(engine)
app = Flask(__name__)
@app.route('/addMember')
def Index():
	return "Hello welcome to home page" 
def addMember():
	return render_template('data.html') 
app.route('/registerUser')
def registerUser():
	id = request.form.get("ID")
	name = request.form.get("name")
	fatherName = request.form.get("father_name") 
	motherName = request.form.get("motner_name") 
	
	print(id,name,fatherName,motherName)
	 
	ins = myData.insert.values(id = id, name = name, father_name = fatherName,mother_name = mother_name)

	conn = engine.connect() 
	
if __name__ == "__main__": 
	app.run(debug=True)
