class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Coordinates: ({self.x}, {self.y})")
point = Point(3, 5)
point.show()
