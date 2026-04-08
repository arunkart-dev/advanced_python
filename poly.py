class Square:
    def area(self):
        l = int(input("Enter a length : "))
        b = int(input("Enter a breadth : "))
        c = l*b
        print("Result : ",c)

class Rectangle:
    def area(self):
        l = int(input("Enter a length peri : "))
        b = int(input("Enter a breadth peri : "))
        d = 2*l*b
        print("Result peri : ",d)


for shape in (Square(),Rectangle()):
    shape.area()
