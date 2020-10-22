n1=float(input('Enter 1st Height\n'))
n2=float(input('Enter 2nd Height\n'))
n3=float(input('Enter 3rd Height\n'))
if n1>n2 and n1>n3:
	print('n1 is the highest')
elif n2>n1 and n2>n3:
	print('n2 is the highest')
else:
	print('n3 is the highest')
