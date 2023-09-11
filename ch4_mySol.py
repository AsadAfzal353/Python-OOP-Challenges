
from functools import total_ordering
from math import sqrt

@total_ordering
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError
        else:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __mul__(self, other):
        if not int(other):
            raise TypeError
        else:
            return Vector(self.x * other, self.y * other, self.z * other)
        
    def __rmul__(self, other):
        if not int(other):
            raise TypeError
        else:
            return self * other
        
    def __gt__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Not an instance of the Vector object!")
        else:
            return (self.__abs__() > other.__abs__())

    def __eq__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Not an instance of the Vector object!")
        return (self.x == other.x and self.y == other.y and self.z == other.z)
    
    def __hash__(self):
        return hash(self.x, self.y, self.z)
    
    def __bool__(self):
        return (self.__abs__() > 0)
    
    def __getitem__(self, item):
        return getattr(self, item.lower())

if __name__ == '__main__':

    v1 = Vector(1, 2, 3)
    v2 = Vector(2, 3, 6)
    v3 = Vector(0, 0, 0)

    v1 + v2 # Vector(3, 5, 9)

    bool(v1) # True

    bool(v3) # False

    abs(v2) == sqrt(49) # True

    v2 * 2 == Vector(4, 6, 12) # True

    assert 2 * v2 == Vector(4, 6, 12) # True

    v1 < v2 # True

    v1 <= v2 # True

    v1 > v2 # False

    v1 == eval(repr(v1)) # True

    v1['x'] # 1

    v2['Y'] # 3

    v3['Z'] # 0

    v3["Andy"] # NotImplemented