#!/usr/bin/python3
"""Module containing Dragon class with mixins"""


class SwimMixin:
    """The SwimMixin class"""
    def swim(self):
        """swim method"""
        print("The creature swims!")


class FlyMixin:
    """The FlyMixin class"""
    def fly(self):
        """fly method"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """The Dragon class"""
    def roar(self):
        """roar method"""
        print("The dragon roars!")
