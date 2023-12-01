str=input("enter a string:  ")
s=str.split()
max=0
for ele in s:
	if len(ele)>max:
		max=len(ele)
		max_word=ele
print("the largest word is : ", max_word)
print("the length of largest word is :" ,len(max_word))









	
