import sqlite3
conn = sqlite3.connect('sampledb.db')
print("db created successfully")
cur = conn.cursor()
conn.execute('''CREATE TABLE students (ID INTEGER, name TEXT, branch TEXT)''')
conn.execute("INSERT INTO students VALUES('21', 'Deepak Reddy', 'CSE')")
conn.execute("INSERT INTO students VALUES('22', 'Robin', 'EEE')")
print("data inserted successfully")
for row in cur.execute('SELECT * FROM students'):
	print(row)


data1 = [('23', 'John', 'CSE'),('24', 'Martin', 'ECE'), ('25','Luther','EEE')]
cur.executemany('INSERT INTO students VALUES(?,?,?);',data1)
print("Inserted multiple data successfully")
for row in cur.execute('SELECT * FROM students'):
	print(row)
