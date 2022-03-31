import math


class MyCircle:

    def __init__(self, radius=None):
        self._radius = radius
        self._area = MyCircle.calculate_area(self)

        if radius is None:
            raise ValueError("Missing argument")
        else:
            self._diameter = self._radius * 2
            

    def calculate_area(self):
        return pow(self._radius, 2) * math.pi

    def __eq__(self, other_circle):
        if not isinstance(other_circle, MyCircle):
            raise TypeError('Can only compare two Circles')
        return self._area == other_circle._area

    def __gt__(self, other_circle):
        if not isinstance(other_circle, MyCircle):
            raise TypeError('Can only calculate between two Circles')
        return self._area > other_circle._area

    def __lt__(self, other_circle):
        if not isinstance(other_circle, MyCircle):
            raise TypeError('Can only calculate between two Circles')
        return self._area < other_circle._area

    def __add__(self, other_circle):
        if not isinstance(other_circle, MyCircle):
            raise TypeError('Can only add between two Circles')
        else:
            return MyCircle(radius=(self._radius + other_circle._radius)) 

    def __radd__(self, other_circle):
        return self.__add__(self, other_circle)


    @property 
    def area(self):
        return self._area

    @property
    def radius(self):
        return self._radius 

    @radius.setter
    def radius(self, value):
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius
    
    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value):
        self.diameter = value

    @diameter.deleter
    def diameter(self):
        del self._diameter