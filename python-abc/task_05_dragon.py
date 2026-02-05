#!/usr/bin/python3
"""
This module defines mixin classes for swimming and flying abilities,
and a Dragon class that demonstrates multiple inheritance using these mixins.
"""


class SwimMixin:
    """
    Mixin class that provides swimming ability to any creature.

    Methods:
        swim(): Prints a message indicating that the creature swims.
    """

    def swim(self):
        """Print that the creature swims."""

        print("The creature swims!")


class FlyMixin:
    """
    Mixin class that provides flying ability to any creature.

    Methods:
        fly(): Prints a message indicating that the creature flies.
    """

    def fly(self):
        """Print that the creature flies."""

        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Represents a Dragon creature that can both swim and fly.

    Inherits:
        SwimMixin: Provides the swim() method.
        FlyMixin: Provides the fly() method.

    Methods:
        roar(): Prints a message indicating that the dragon roars.
    """

    def roar(self):
        """Print that the dragon roars."""
        print("The dragon roars!")
