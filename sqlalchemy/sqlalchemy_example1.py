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
meta.create_all(engine)
ins  = myData.insert().values(id = 124,name = 'Deepak', father_name = 'saireddy',mother_name='chandrakala')
ins1 = [
	[122,"Deepak2", "saireddy2","chandrakala2"],
	[123,"Deepak3", "saireddy3","chandrakala3"],
	[124,"brek","thomaz","julia"],
	[125,"john","alex","mary"]
]
engine.execute(myData.insert().values(ins1)) 
conn = engine.connect()
x = myData.select() 
result = conn.execute(x)
for row in result:
	print (row)

b = myData.update().where(myData.c.name=='brek').values(name='dyvtva') 
conn.execute(b) 
y = myData.select() 
conn.execute(y).fetchall()
result = conn.execute(y) 
for row in result:
	print(row)
