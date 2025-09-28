#!/usr/bin/python3
"""Module containing BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class based on BaseGeometry class"""

    def __init__(self, width, height) -> None:
        """Initializing for Rectangle object"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Area calculator function"""
        return self.__width * self.__height

    def __str__(self):
        """Printing the Rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
