def func(a,b):
	sum=a+b
	return sum



x=int(input('Enter the value of a\n'))
y=int(input('Enter the value of b\n'))
if x>=10 and y>=10:
	z=func(x,y)
	print("The sum of the numbers is",z)
else:
	print("Invalid input")



