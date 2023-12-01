a=[]
n= int(input("enter the element:"))
for x in range (0,n):
	element=input("enter the word: ")
	a.append(element)
max=len(a[0])
temp=a[0]
for i in a:
	if len(i)>max:
		max=len(i)
		temp=len(i)
print("the lenght of the largest word is",temp)
