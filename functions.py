

def my_function(x, y, z=3):
	if z > 1:
		print z * (x + y)
		return z * (x + y)
	else:
		print z / (x + y)
		return z / (x + y)


a = 5
b = 6
c = .7

#notice that the default z value of 3 if overridden
my_function(a, b, c)


print("and now a new function with lists")

a = []

def func():
	for i in range(5):
		a.append(i)

# returns [0, 1, 2, 3, 4] notice how it starts at 0
func()

print a


