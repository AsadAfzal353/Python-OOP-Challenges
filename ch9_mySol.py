
class Point3D:

    __slots__ = ('x', 'y', 'z')

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        classname = self.__class__.__name__
        extrastr = ""

        if classname != "Point3D":
            name = self.__class__.__slots__[0]
            value = getattr(self, name)
            extrastr = f", {name}='{value}'"
             
                
        return f"{type(self).__name__}(x={self.x}, y={self.y}, z={self.z}{extrastr})"
    
class ColoredPoint(Point3D):

    __slots__ = ('color',)

    def __init__(self, *args, color="black", **kwargs):
        self.color = color
        super().__init__(*args, **kwargs)

class ShapedPoint(Point3D):

    __slots__ = ('shape',)

    def __init__(self, *args, shape="sphere", **kwargs):
        self.shape = shape
        super().__init__(*args, **kwargs)


if __name__ == "__main__":

    p = Point3D(1, 2, 3)
    p

    p.__dict__ # AttributeError: 'Point3D' object has no attribute '__dict__'

    cp = ColoredPoint(1, 4, 9, color="blue")

    cp.__dict__ # AttributeError: 'ColoredPoint' object has no attribute '__dict__'

    sp = ShapedPoint(1, 2, 9, shape="sphere")

    sp = ShapedPoint(1, 2, 9)
    sp.__dict__ # AttributeError: 'ShapedPoint' object has no attribute '__dict__'

    sp.name = "spherical" # AttributeError: 'ShapedPoint' object has no attribute 'name'

    sp.shape = "cube"
    sp # ShapedPoint(x=1, y=2, z=9, shape='cube')

    cp # ColoredPoint(x=1, y=4, z=9, color='blue')

    p # Point3D(x=1, y=2, z=3)