class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        c = self.length * self.breadth
        print("Result is : ",c)
l = int(input("Enter length : "))
b = int(input("Enter breadth "))

r1 = Rectangle(l,b)
r1.area()





