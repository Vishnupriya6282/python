def power(b,e):
	if e==0:
  		return 1
	elif e==1:
	        return n
	else:
  		return b*power(b,e-1)
n=int(input("enter the base"))
m=int(input("enter the exponent"))
print(power(n,m))
