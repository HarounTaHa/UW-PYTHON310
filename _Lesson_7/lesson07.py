class C:
    this = 5

    def __init__(self, that):
        self.that = that


c1 = C(10)
c2 = C(20)
print(c1 is c2)
print(c1.this)
print(c2.this)
print(c1.that)
print(c2.that)

C.this = 45

print(c1.this)


class Point:
    # everything defined in here is in the class namespace
    def __init__(self, x, y):
        self.x = x
        self.y = y

