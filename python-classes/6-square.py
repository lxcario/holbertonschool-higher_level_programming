#!/usr/bin/python3
"""Module for creating Square class"""


class Square:
    """A class representing Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with a given size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for the size of square"""
        return self.__size

    @property
    def position(self):
        """Getter for the position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter for the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setter for the position of the square"""
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) for num in value) and
                all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return of the area of square"""
        return self.__size**2

    def my_print(self):
        """Print the square to stdout"""
        if self.size == 0:
            print()
        else:
            print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(self.__position[0] * " " + self.size * "#")
