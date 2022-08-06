import csv 

header = ['Reg Num', 'Name', 'Section'] 
data1 =




with open('studentdata1.csv', 'w') as f:
	writer = csv.writer(f) 
	#write the header 
	writer.writerow(header) 
	#write the data
	writer.writerow(data1) 

	#writing multiple data into the csv
with open('studentdata1.csv', 'a') as f:
	writer = csv.writer(f) 
	writer.writerows(data2) 
	
print("Writing of data successfully done") 

	#Reading multiple data from csv 
with open('student
