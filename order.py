n=int(input("enter the number of names:"))
names=[]
for i in range(n):
	name=input("enter the name:")
	names.append(name)
	names.sort()
print("sorted names:")
for name in names:
	print(name)
