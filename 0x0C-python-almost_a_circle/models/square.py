#!/usr/bin/python3
"""module for square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''Size of this square.'''
        return self.__width

    @size.setter
    def size(self, value):
        self.__width = value
        self.__height = value

    def __str__(self):
        return f"[{type(self).__name__}] ({self.id}) {self.x}/{self.y} - {self.width}"

    def __updatein(self, id=None, size=None, x=None, y=None):
        """ private method to validate arguments and update attributes"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
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
        """Returns dictionary representation of this class."""
        return {"id": self.id, "size": self.width,"x": self.x, "y": self.y}
    


