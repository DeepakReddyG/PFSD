def addition(x,y):
	print(x+y)
def subtraction(x,y):
	print(x-y)
print("select operation: ")
print('1.Addition')
print('2.Subtraction')

print("Enter your choice: ")
choice = int(input())
if (choice == 1):
	addition(int(input("Enter number: ")),int(input("Enter number:")))
else:
	subtraction(int(input("Enter number: ")),int(input("Enter number:")))
