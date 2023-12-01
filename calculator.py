def add(a,b):
	c=a+b
	return c
def sub(a,b):
	c=a-b
	return c
def mul(a,b):
	c=a*b
	return c
def div(a,b):
	c=a/b
	return c
def power(a,b):
	c=a**b
	return c
n=float(input("enter the first number"))
m=float(input("enter the second number"))
print("1.+   2.-   3. *  4. /  5.**")
choice=input("enter the choice")
if choice=="+":
	print("the result is" ,add(n,m))
elif choice=="-":
	print("the result is" ,sub(n,m))
elif choice=="*":
	print("the result is",mul(n,m))
elif choice=="/":
	print("the result is",div(n,m))
elif choice=="**":
	print("the result is",power(n,m))
else:
	print("invalid power")
	
