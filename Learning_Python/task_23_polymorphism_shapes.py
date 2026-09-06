"""টাস্ক: একটি প্যারেন্ট ক্লাস বানাও Shape যার ভেতর একটি মেথড থাকবে area() যা প্রিন্ট করবে Area not defined।দুটি চাইল্ড ক্লাস বানাও: Square (যার বাহু length থাকবে এবং area() রিটার্ন করবে $length \times length$) এবং Rectangle (যার width ও height থাকবে এবং area() রিটার্ন করবে $width \times height$)।উভয় ক্লাসের অবজেক্ট বানিয়ে area() মেথড কল করো।"""

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
