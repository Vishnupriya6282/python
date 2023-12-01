def reverse(num):
 rev=0
 while num>0:
  rev=rev*10+(num%10)
  num=num//10
 return rev
num=int(input("enter any number"))
ans= reverse(num)
if num==ans:
  print("number is palindrome")
else:
 print("number is not palindrome")

