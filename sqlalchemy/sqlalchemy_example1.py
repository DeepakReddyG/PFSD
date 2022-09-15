from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///myTable.db',echo = True) 
meta = MetaData()
myData = Table(
	'myData', meta,
	Column('id', Integer,primary_key = True),
	Column('name',String),
	Column('father_name',String),
	Column('mother_name',String)
)	
conn  = engine.connect() 
x = myData.select() 

