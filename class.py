class rect():
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		c=self.length*self.breadth
		print("area of rectangle:",c)
	def perimeter(self):
		p=2*(self.length+self.breadth)
		print("perimeter of the rectangle:",p)
a=int(input("enter the length :"))
b=int(input("enter the breadth:"))
obj=rect(a,b)
obj.area()
obj.perimeter()
