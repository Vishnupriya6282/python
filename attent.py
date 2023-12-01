STUDENT=int(input("ENTER TOTAL NUMBER OF STUDENTS:"))
m=int(input("ENTER TOTAL PRESENT DAYS:"))
l=[ ]
for i in range(0,STUDENT):
	s=input("ENTER THE NAME OF STUDENT:")
	d=int(input("ENTER STUDENT PRESENT DAYS:"))
	percent=int((d/m)*100)
	l.append((s,percent))
print("ATTENDANCE IS :",l)
l.sort(reverse=True)
print("SORTED IN DESCENDING ORDER: ")
for j in l:
	print(j)


