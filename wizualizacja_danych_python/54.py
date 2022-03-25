class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstruktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)

p1 = Point(2,1)
p2 = Point(3,7)
p3 = Point(0,2)
p4 = Point(0,4)
p5 = Point(2,0)
p6 = Point(0,5)

print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print(p5.counter)
print(p6.counter)
p1.update(10)
p2.update(16)
p3.update(2)
p4.update(23)
p5.update(3)
p6.update(66)
print(p1.counter)
print(p2.counter)
print(p3.counter)
print(p4.counter)
print(p5.counter)
print(p6.counter)

