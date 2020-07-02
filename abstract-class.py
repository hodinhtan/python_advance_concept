from abc import ABC, abstractmethod

class Polygon(ABC):

    @abstractmethod
    def draw(self):
        pass
    def getArea(self):
        pass
    def getCircuit(self):
        pass
    @abstractmethod
    def xaoxao(self):
        pass
class Rectangle(Polygon):
    def __init__(self, w ,h ):
        self.w = w
        self.h = h
    def draw(self):
        print("rectangle draw")

    def getArea(self):
        return self.w * self.h
    def getCircuit(self):
        return (self.w+self.h) * 2
    def xaoxao(self):
        print ("fuck u bitch")
class Square(Polygon):
    def __init__(self, side ):
        self.side = side
    def draw(self):
        print("rectangle draw")

    def getArea(self):
        return self.side ** 2
    def getCircuit(self):
        return (self.side * 4)
    def xaoxao(self):
        print ("love u bitch")
rec = Rectangle(2,3)
sq = Square(5)

print(rec.getArea(), sq.getCircuit())