#Question 2 set9 week 3
class Shape:
    count=1
    def __init__(self,x):
        self.s1=x
    def setSide(self,side):
        self.side=side
    def getSide(self):
        return self.side
a = Shape(100)
a.setSide(5)
print(a.getSide())
