#!/usr/bin/python3
"""Module containing BaseGeometry class functions"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class based on Rectangle class"""

    def __init__(self, size):
        """Initializing for Square object"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Area calculator function"""
        return self.__size * self.__size

    def __str__(self):
        """Printing the Square"""
        return f"[Square] {self.__size}/{self.__size}"
