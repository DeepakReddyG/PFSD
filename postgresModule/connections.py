import psycopg2
from psycopg2 import Error
try:
	connection = psycopg2.connect(user = "deepakreddygathpa", password = '**********',host ="127.0.0.1",port 
= "5432", database="test") 
	cursor = connection.cursor()
	insert_query = """ INSERT INTO students (ID,Name,IDN) VALUES (1,"John","123") """
	cursor.execute(insert_query)
	connection.commit()
	print("1 record inserted successfully")
	cursor.execute("SELECT * from students")
	record = cursor.fetchall()
	print("result ",record) 
	print("PostgreSQL Server Information")
	print(connection.get_dsn_parameters(), "\n")
	cursor.execute("SELECT version();") 
	record = cursor.fetchone()
	print("You are connected to - ",record,"\n")
except(Exception,Error) as error:
	print("Error while connecting to PostgreSQL",error)
finally:
	if(connection):
		cursor.close()
		connection.close()
		print("postgreSQL connection is closed")
