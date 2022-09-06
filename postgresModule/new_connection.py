import psycopg2
from psycopg2 import Error

hostname = "127.0.0.1"
database = "test"
username = "deepakreddygathpa"
pwd = "12345"
port_id = "5432"

conn = psycopg2.connect(
	host = hostname,
	database = database,
	user = username,
	password = pwd,
	port = port_id) 

if(conn):
	print("Success")
	print(conn.get_dsn_parameters())
else:
	print("Unable to connect")
conn.close()
