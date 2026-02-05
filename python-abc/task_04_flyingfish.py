#!/usr/bin/python3
"""
Construct a FlyingFish class that inherits
from both a Fish class and a Bird class.
Within FlyingFish, override methods from both parents.
The goal is to comprehend multiple inheritance
and how Python determines method resolution order.
"""


class Fish:
    """
    Represents a fish with basic swimming behavior and habitat.

    Methods:
        swim(): Prints a message indicating that the fish is swimming.
        habitat(): Prints the habitat of the fish (water).
    """

    def swim(self):
        """Print that the fish is swimming."""

        print("The fish is swimming")

    def habitat(self):
        """Print that the fish lives in water."""

        print("The fish lives in water")


class Bird:
    """
    Represents a bird with basic flying behavior and habitat.

    Methods:
        fly(): Prints a message indicating that the bird is flying.
        habitat(): Prints the habitat of the bird (sky).
    """

    def fly(self):
        """Print that the bird is flying."""

        print("The bird is flying")

    def habitat(self):
        """Print that the bird lives in the sky."""

        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Represents a flying fish, which inherits from both Fish and Bird.

    Overrides methods from both parents to reflect combined behavior.

    Methods:
        fly(): Prints that the flying fish is soaring.
        swim(): Prints that the flying fish is swimming.
        habitat(): Prints that the flying fish lives both in water and the sky.
    """

    def fly(self):
        """Print that the flying fish is soaring."""

        print("The flying fish is soaring!")

    def swim(self):
        """Print that the flying fish is swimming."""

        print("The flying fish is swimming!")

    def habitat(self):
        """Print that the flying fish lives both in water and the sky."""

        print("The flying fish lives both in water and the sky!")
