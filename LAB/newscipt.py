import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["deepak"]
mycol = mydb["deepak"]
#dblist = myclient.list_database_names()
myquery = { "name":"Deepak","age":19,"status":"single"}
#print(myclient.list_database_names())
a = mycol.insert_one(myquery)
newvalues = { "$set": { "age": "18" } }
mycol.update_one(myquery, newvalues)
#print(myclient.list_database_names())
for x in mycol.find():
  print(x)
