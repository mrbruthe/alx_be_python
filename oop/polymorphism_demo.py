# polymorphism_demo.py

import math

class Shape:
    """Base class representing a geometric shape."""
    def area(self):
        """Should be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    """Represents a rectangle shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Returns the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Represents a circle shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Returns the area of the circle."""
        return math.pi * (self.radius ** 2)
