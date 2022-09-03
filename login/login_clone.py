from pymongo import MongoClient
client = MongoClient('mongodb://localhost:270717/')
db = client['PFSD']
info = db.PFSD
student1 = {"Reg Num": "2100031817","Name":"Deepak Reddy"}
student2 = [
	{"Reg Num": "2100012345","Name":"ABCD"},
	{"Reg Num": "2100012346","Name":"EFGH"},
	{"Reg Num": "2100012347","Name":"IJKL"},
] 

app  = Flask(__name__)


#creating our routes
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

@app.route("/login")
def my_index_page():
    return render_template("login.html")

@app.route("/newuser")
def my_newuser_register_page():
    return render_template("newuserregister.html")

@app.route("/registeruser", methods=['POST','GET'])
def my_regiser_user():
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")
    entered_password = entered_password.lower()
    entered_email = request.form.get("email")
    entered_mobileno = request.form.get("mobileno")

    print(entered_username, entered_password, entered_email, entered_mobileno)

    con = sqlite3.connect("my_database.sqlite3")

    cur = con.cursor()

    my_table_query = "create table if not exists userstable(name varchar(20),password varchar(15),email varchar(30),mobileno varchar(10))"
    cur.execute(my_table_query)

    cur.execute(f"select email from userstable where email='{entered_email}'")
    result = cur.fetchone()
    if result != None:
        return "Email Already Exists....Try again"
    else:
        my_insert_query = f"insert into userstable values('{entered_username}','{entered_password}','{entered_email}','{entered_mobileno}')"
        cur.execute(my_insert_query)
        con.commit()
        return "User Registered Successfully"

@app.route("/loginuser", methods=['POST','GET'])
def my_login():
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")
    con = sqlite3.connect("my_database.sqlite3")
    cur = con.cursor()
    cur.execute(f"select * from userstable where name='{entered_username}' and password='{entered_password}'")

    result = cur.fetchone()
    if result is None:
        return "Invalid User Credentials....try again"
    else:
        return "login success"

#run flask app
if __name__ == "__main__":
    app.run(debug=True)
