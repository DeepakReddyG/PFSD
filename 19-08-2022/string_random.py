import random
import string

for i in range(3):
	result_str = ''.join(random.sample(string.ascii_lowercase,8))
	print(result_str)
