from math import sqrt

class City(object):
    
    def __init__(self, x, y):
        self.x = x
        self.y = y    

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
    
    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __repr__(self):
        return "<city.City {}>".format(str(self)) 

    def __getitem__(self, item):
        if item == "x":
            return self.x
        if item == "y":
            return self.y
        raise KeyError

    def distanceTo(self, target):
        return sqrt( ( ( target.x - self.x ) ** 2 ) + 
                     ( ( target.y - self.y ) ** 2 ))