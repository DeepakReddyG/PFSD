#python program to add two numbers

class Addition:
	a = 0
	b = 0
	result = 0
	
	#parameterized constructor in python 
	def __init__(self,f,s):
		self.a = f
		self.b = s

	
	def display(self):
		print("first number = ",self.a)
		print("second number = ",self.b)
		print("result = ",self.result)
	
	def calculate(self):
		self.result = self.a+self.b
obj = Addition(int(input('Enter first value: ')),int(input('Enter second number:')))
obj.calculate()
obj.display()

