f=open('text.txt','w')
s=input("Enter the text of your wish\n")
f.write(s)
v='AaEeIiOoUu'
res=set([each for each in s if each in v])
f.write(str(res))
print('file saved')
f.close()