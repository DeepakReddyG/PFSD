import psycopg2
from psycopg2 import Error

host_name = "127.0.0.1"
db_name = "test"
user_name = "deepakreddygathpa"
pwd = "12345"
port_id = "5432"


conn = psycopg2.connect(host = host_name,
		database = db_name,
		user = user_name,
		password = pwd,
		port = port_id)

if(conn):
	print('success')
else:
	print("Connection failed")

cur = conn.cursor()

create_script = '''CREATE TABLE Kids (
			id	int PRIMARY KEY,
			Name	varchar(20) NOT NULL,
			age	int NOT NULL)''' 

cur.close() 
conn.close()


	
