class Rectangle:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        # Write your code 
        return 2*(self.l+self.b)


class Square:
    def __init__(self,s):
        self.s = s
    def area(self):
        # Write your code 
        return 4 * self.s
l = int(input())
b = int(input())
s = int(input())

shapes = [Rectangle(l,b),Square(s)]
for shape in shapes:
    print(shape.area())

# R = Rectangle(l,b)
# S = Square(s)

