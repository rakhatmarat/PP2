import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates of the point: ({}, {})".format(self.x, self.y))

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

x1 = float(input("Enter x-coordinate of point 1: "))
y1 = float(input("Enter y-coordinate of point 1: "))
x2 = float(input("Enter x-coordinate of point 2: "))
y2 = float(input("Enter y-coordinate of point 2: "))

point1 = Point(x1, y1)
point2 = Point(x2, y2)

point1.show()

new_x = float(input("Enter new x-coordinate for point 1: "))
new_y = float(input("Enter new y-coordinate for point 1: "))
point1.move(new_x, new_y)
point1.show()

distance = point1.dist(point2)
print("Distance between point1 and point2:", distance)
