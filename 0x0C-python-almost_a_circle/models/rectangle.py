#!/usr/bin/python3
"""class rectangle module"""
from base import Base

class Rectangle(Base):
    """Rectangle class methods and attributes"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """class constructor"""
        self.validate("width", width)
        self.validate("height", height)
        self.validate("x", x)
        self.validate("y", y)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def validate(self, name, value):
        """ validate rectangle attributes"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if name in ["width","height"] and value <= 0:
            raise ValueError(f"{name} must be > 0")
        if name in ["x", "y"] and value < 0:
            raise ValueError(f"{name} must be >= 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
       self.validate("height", value)
       self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validtae("y", value)
        self.__y = value
    
    def area(self):
        """return the area of rectangle"""
        return self.__height*self.__width
    
    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        out = '\n' * self.y + (' ' * self.x + '#' * self.width + '\n') * self.height
        print(out, end='')

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    
     def __updatein(self, id=None, width=None, height=None, x=None, y=None):
        """ private method to validate arguments and update attributes"""
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update attributes with no keywords"""
        if args:
            self.__updatein(*args)
        elif kwargs:
            self.__updatein(**kwargs)

    
    def to_dictionary(self):
        return {"id": self.id, "width": self.__width, "height": self.__height,"x": self.__x, "y": self.__y}


