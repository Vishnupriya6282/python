student={ }
num=int(input("enter the number ofstudent: "))
for i in range(0,num):
	name=input("enter the name of student: ")
	age=input("enter the age of student: ")
	grade=input("enter the grade of student: ")
	student[name]=age,grade
print(student)
