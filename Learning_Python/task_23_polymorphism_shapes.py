class Shape :
    def area(self):
        print("Area not defined.")


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length


class Rectangle(Shape):
    def __init__(self, width , height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

sq = Square(5)
rect = Rectangle(4, 6)

print (f"Square Area : {sq.area()}")
print (f"Rectangle Area : {rect.area()}")
