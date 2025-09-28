#!/usr/bin/python3
"""Module containing Animal class and its inheritances"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """The Animal class"""
    @abstractmethod
    def sound(self):
        """Method to make sound"""
        pass


class Dog(Animal):
    """Dog class Inherited from Animal"""
    def sound(self):
        """Dog goes Bark"""
        return "Bark"


class Cat(Animal):
    """Cat class Inherited from Animal"""
    def sound(self):
        """Cat goes Meow"""
        return "Meow"
