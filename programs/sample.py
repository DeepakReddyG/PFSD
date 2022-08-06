import psycopg2

conn = psycopg2.connect(
	database = "school", 
	user = "postgres", 
	password = "demo1234", 
	host = "localhost" , 
	port = "5432"
) 
print("connected to postgres DB")
