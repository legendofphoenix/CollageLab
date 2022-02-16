#Question 3
class Rectangle():
    def __init__(self):
        self.length = int(input("Enter Length : "))
        self.width = int(input("Enter width : "))
    def rectangle_area(self):
        return self.length*self.width
    def rectangle_perimeter(self):
        return 2*(self.length+self.width)

newRectangle = Rectangle()
print("Area = ",newRectangle.rectangle_area())
print("Perimeter = ",newRectangle.rectangle_perimeter())
