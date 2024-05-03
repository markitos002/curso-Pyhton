#class

class Point():
    def __init__(self, x, y):  # constructor, init is the method name and self is the first parameter
        self.x = x
        self.y = y

p = Point(3, 5)

print(p.x , p.y)