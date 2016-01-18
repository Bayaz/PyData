

def my_function(x, y, z=3):
	if z > 1:
		print z * (x + y)
		return z * (x + y)
	else:
		print z / (x + y)

a = 5
b = 7

my_function(a, b)