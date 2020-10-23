f=open('emp.txt','w')
i=0
while i<10:
	id=int(input('Enter the id of 10 employees\n'))
	f.write(str(id))
	name=input('Enter the name of 10 employees\n ')
	f.write(name)
	salary=int(input('Enter the salary of 10 employees\n'))
	f.write(str(salary))
	i=i+1


print('file saved')
f.close()