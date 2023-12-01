def pal(a):
	s=str(a)
	return (s==s[::-1])
a = str(input("enter a number to check:")) 
if (pal(a)):
	print("yes the number is a palindrome")
else:
	print("no the number is not a palindrome")
