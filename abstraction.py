from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def peri(self):
        pass
class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        print("Area : ",3.14*self.r*self.r)
    def peri(self):
        print("Peri ",4*self.r)
class Vad(Shape):
    def __init__(self,y):
        self.y = y
    def area(self):
        print("Area : ",self.y*self.y)
    def peri(self):
        print("Perimeter : ",4*self.y)
c = Circle(5)
c.area()
v = Vad(6)
v.peri()
