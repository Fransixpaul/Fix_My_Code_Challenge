#!/usr/bin/python3

class Square:
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        if self.width != self.height:
            raise ValueError("Width and height must be equal for a square")

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.width

    def perimeter_of_my_square(self):
        """Perimeter of the square"""
        return 4 * self.width

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
