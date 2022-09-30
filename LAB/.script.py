import pymongo
from pymongo import MongoClient
myClient = pymongo.MongoClient("mongodb://localhost:27017/") 
mydb = myClient("Employee")
collec = mydb["emp"]
attributes = {"name":"deepak","age":19,"status":"single"}
a = collec.insert_one(attributes)
newq = {"age":19}
collec.delete_one(newq)
for x in collec.find():
	print(x)
