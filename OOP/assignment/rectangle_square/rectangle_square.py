class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def __repr__(self):
        return f"{__class__.__name__}(width={self.width}, height={self.height})"

    def __str__(self):
        return f"The {__class__.__name__} has a width of {self.width}cm and a height of {self.height}cm"


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        self.length = length

    def __repr__(self):
        return f"{__class__.__name__}(length={self.length})"

    def __str__(self):
        return f"The {__class__.__name__} has a length of {self.length}cm"


rectangle = Rectangle(4, 2)
print(rectangle)
print(f"The rectangle has an area of {rectangle.get_area()}cm squared")
print(f"The rectangle has a perimeter of {rectangle.get_perimeter()}cm")

square = Square(2)
print(square)
print(f"The square has an area of {square.get_area()}cm squared")
print(f"The square has a perimeter of {square.get_perimeter()}cm")
