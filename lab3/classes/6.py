import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        distance = math.sqrt(dx ** 2 + dy ** 2)
        return distance

# Taking user input to initialize points
x1 = float(input("Enter x coordinate for point 1: "))
y1 = float(input("Enter y coordinate for point 1: "))
point1 = Point(x1, y1)

x2 = float(input("Enter x coordinate for point 2: "))
y2 = float(input("Enter y coordinate for point 2: "))
point2 = Point(x2, y2)

point1.show()
point2.show()

print("Distance between point1 and point2:", point1.dist(point2))

# Moving points based on user input
new_x1 = float(input("Enter new x coordinate for point 1: "))
new_y1 = float(input("Enter new y coordinate for point 1: "))
point1.move(new_x1, new_y1)

new_x2 = float(input("Enter new x coordinate for point 2: "))
new_y2 = float(input("Enter new y coordinate for point 2: "))
point2.move(new_x2, new_y2)

point1.show()
point2.show()

print("Distance between point1 and point2 after moving:", point1.dist(point2))
