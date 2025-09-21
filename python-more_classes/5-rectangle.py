#!/usr/bin/python3
"""Module containing Rectangle class"""


class Rectangle:
    """Class representing rectangle"""

    def __init__(self, width=0, height=0):
        """Initialization of Instance"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for __width"""
        return self.__width

    @property
    def height(self):
        """Getter for __height"""
        return self.__height

    @width.setter
    def width(self, value):
        """Setter for width"""

        # Checking if value is not valid
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter for height"""

        # Checking if value is not valid
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to return area"""
        return self.__height * self.__width

    def perimeter(self):
        """Method to return perimeter"""

        # Checking if height and width is equal to 0
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Method to print the rectangle"""

        # Checking if height and width is equal to 0
        if self.__height == 0 or self.__width == 0:
            print()
        else:

            # Creating string for printing
            rectangle = ""
            for i in range(self.__height - 1):
                rectangle += (self.__width * "#" + '\n')
            rectangle += (self.__width * "#")
            return rectangle

    def __repr__(self):
        """Method to return recreateable instance"""

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Method to print "Bye rectangle..." when an instance is deleted"""
        print("Bye rectangle...")
