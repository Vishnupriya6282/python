student={ }
num=int(input("enter the number of students:"))
for i in range (0,num):
	name=input("enter the name of student: ")
	grade=input("enter the  grade of student: ")
	student[name]=grade
print("list of student :",student)
a=list(student.items())
a.sort()
print("sorted in ascending order",a)
b=list(student.items())
b.sort(reverse=True)
print("sorted in descending order:",b)

