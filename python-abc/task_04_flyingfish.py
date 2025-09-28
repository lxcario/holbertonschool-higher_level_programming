#!/usr/bin/python3
"""Module for FlyingFish class"""


class Fish:
    """The Fish class"""

    def swim(self):
        """Swim method"""
        print("The fish is swimming")

    def habitat(self):
        """Habitat method"""
        print("The fish lives in water")

class Bird:
    """The Bird class"""

    def fly(self):
        """Fly method"""
        print("The bird is flying")

    def habitat(self):
        """Habitat method"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """The FlyingFish class"""

    def fly(self):
        """Override of fly method"""
        print("The flying fish is soaring!")

    def swim(self):
        """Override for swim method"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override for habitat method"""
        print("The flying fish lives both in water and the sky!")
