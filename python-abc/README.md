<a href="#"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# Python OOP - Abtract Class, Interface, Subclassing

* ## **[0. Abstract Animal Class and its Subclasses](task_00_abc.py)**

## Background:
In object-oriented programming, Abstract Base Classes (ABCs) ensure that derived classes implement specific methods from the base class. This provides a blueprint for creating and structuring derived classes. Python's ```ABC``` package facilitates the creation of abstract base classes.

## Objective:
Create an abstract class named ```Animal``` using the ```ABC``` package. This class should have an abstract method called ```sound```.
Create two subclasses of ```Animal```: ```Dog``` and ```Cat```. Implement the sound method in each subclass to return the strings “Bark” and “Meow” respectively.

## Resources:
Python ```ABC``` documentation: https://docs.python.org/3/library/abc.html

## Instructions:
1. **Setting up the Abstract Class**:
* Import the necessary components from the ```abc``` module.
* Define the ```Animal``` class, ensuring it inherits from ```ABC``` to mark it as abstract.
* Inside the ```Animal``` class, declare an abstract method named ```sound``` using the ```@abstractmethod``` decorator.

1. **Implementing the Subclasses**:
* Create a subclass named ```Dog``` that inherits from the ```Animal``` class.
  * Implement the ```sound``` method in the ```Dog``` class to return the string “Bark”.
* Similarly, create a subclass named ```Cat``` that also inherits from the ```Animal``` class.
  * Implement the ```sound``` method in the ```Cat``` class to return the string “Meow”.

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    
class Dog(Animal):
    def sound(self):
        return "Bark"
    
class Cat(Animal):
    def sound(self):
        return "Meow"

```
</details>

---

* ## **[1. Shapes, Interfaces, and Duck Typing](task_01_duck_typing.py)**

## Background:
Python employs a concept called "duck typing," which is concerned with the semantics of objects rather than their inheritance hierarchy. If an object behaves like a duck (i.e., has all the methods and properties of a duck), then it's considered a duck, regardless of its actual class. This concept allows for flexible and dynamic polymorphism.

In this exercise, we'll use abstract base classes to design a blueprint for shapes and use duck typing to handle objects of different shapes uniformly.

## Objective:
1. Create an abstract class named ```Shape``` with two abstract methods: ```area``` and ```perimeter```.
2. Implement two concrete classes: ```Circle``` and ```Rectangle```, both inheriting from ```Shape```. Each class should provide implementations for the ```area``` and ```perimeter``` methods.
3. Write a standalone function named ```shape_info``` that accepts an object of type ```Shape``` (by duck typing) and prints its area and perimeter.
4. Test the ```shape_info``` function with instances of both ```Circle``` and ```Rectangle```.

## Resources:
* Python ```ABC``` documentation: https://docs.python.org/3/library/abc.html
* Concept of Duck Typing: https://realpython.com/lessons/duck-typing/

## Instructions:
1. **Shape Abstract Class**:
* Define an abstract class ```Shape``` using the ```ABC``` package.
* Within ```Shape```, declare two abstract methods: varea``` and ```perimeter```.
1. **Circle and Rectangle Classes**:
* Create a ```Circle``` class that inherits from ```Shape```. The constructor (```__init__```) should accept a radius. Implement the ```area``` and ```perimeter``` methods.
* Create a ```Rectangle``` class, also inheriting from ```Shape```. Its constructor should accept the width and height. Implement the ```area``` and ```perimeter``` methods.
1. **shape_info Function**:
* Define a function named ```shape_info``` that takes a single argument.
* Without explicitly checking the type of the argument, call its ```area``` and ```perimeter``` methods (relying on duck typing).
* Print the area and perimeter of the shape passed to the function.
1. **Testing**:
* Instantiate a ```Circle``` and a ```Rectangle```.
* Pass each object to the ```shape_info``` function and observe the output.

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Defines shapes using abstract base classes."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""
    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""

    def __init__(self, radius):
        """Initialize a circle with a given radius."""
        self.radius = abs(radius)

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Class representing a rectangle."""
    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return self.width * 2 + self.height * 2


def shape_info(obj):
    """Print the area and perimeter of a shape."""
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
```
</details>

---


* ## **[2. Extending the Python List with Notifications](task_02_verboselist.py)**

## Background:
In Python, you can extend built-in classes to add or modify behavior. The ```list``` class provides a collection of methods and functionalities that handle list operations. By extending the ```list``` class, you can provide custom behaviors while retaining the original functionalities.

## Objective:
Create a class named ```VerboseList``` that extends the Python ```list``` class. This custom class should print a notification message every time an item is added (using the ```append``` or ```extend``` methods) or removed (using the ```remove``` or ```pop``` methods).

## Instructions:
1. **Setting up the VerboseList Class**:
* Define a class ```VerboseList``` that inherits from the built-in ```list``` class.
* Within ```VerboseList```, override the methods that modify the list: ```append```, ```extend```, ```remove```, and ```pop```.
1. **Implementing Notifications**:
* For the ```append``` method: After adding the item to the list, print a message like "Added [item] to the list."
* For the ```extend``` method: After extending the list, print a message like "Extended the list with [x] items." where [x] is the number of items added.
* For the ```remove``` method: Before removing the item from the list, print a message like "Removed [item] from the list."
* For the ```pop``` method: Before popping the item from the list, print a message like "Popped [item] from the list." If the index is not specified, default behavior is to pop the last item.
1. **Testing**:
* Instantiate a ```VerboseList``` object.
* Test all the overridden methods (```append```, ```extend```, ```remove```, and ```pop```) and ensure that the appropriate messages are printed for each operation.

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Extends the Python list class and prints a notification message"""


class VerboseList(list):
    """
    A subclass of Python's built-in list that prints a notification
    whenever items are added or removed.
    """
    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        """Extend the list with multiple items and print a notification."""
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=None):
        """Remove and return an item and print a notification."""
        item = self[-1] if index is None else self[index]
        print("Popped [{}] from the list.".format(item))
        if index is None:
            return super().pop()
        else:
            return super().pop(index)
```
</details>

---


* ## **[3. CountedIterator - Keeping Track of Iteration](task_03_countediterator.py)**

## Background:
Subclassing allows a new class to inherit properties and methods from an existing class. In Python, many built-in classes can be extended to customize or enhance their behavior. The ```iter``` function, which returns an iterator object, provides the ```__next__``` method to fetch the next item in the sequence. This exercise focuses on extending the functionality of this iterator object.

## Objective:
Create a class named ```CountedIterator``` that extends the built-in iterator obtained from the ```iter``` function. The ```CountedIterator``` should keep track of the number of items that have been iterated over. Specifically, you will need to override the ```__next__``` method to increment a counter each time an item is fetched.

## Instructions:
1. **Setting up the CountedIterator Class**:
Define a class ```CountedIterator```.
In the constructor (```__init__```), initialize two attributes: the iterator object (using the ```iter``` function) and a counter to track the number of items iterated.
Provide a method ```get_count``` to return the current value of the counter.
1. **Overriding the next Method**:
Within the ```CountedIterator``` class, override the ```__next__``` method.
In this method, increment the counter each time the ```__next__``` method is called.
Fetch the next item from the original iterator and return it. If there are no items left to iterate, the method should raise the ```StopIteration``` exception.
1. **Testing**:
Instantiate a ```CountedIterator``` object using a list or another iterable.
Iterate over items using a loop or manual calls to the ```__next__``` method.
Use the ```get_count``` method to retrieve and print the number of items that have been fetched.

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Extends the built-in iterator obtained from the iter function."""


class CountedIterator:
    """
    An iterator that wraps any iterable
    and counts how many items have been iterated over.
    """

    def __init__(self, iterable):
        """Initialize the CountedIterator with an iterable."""

        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Return the number of items iterated so far"""

        return self.count

    def __iter__(self):
        """Return the iterator object itself."""

        return self

    def __next__(self):
        """Fetch the next item from the iterator and increment the count."""
        item = next(self.iterator)
        self.count += 1
        return item
```
</details>

---


* ## **[4. The Enigmatic FlyingFish - Exploring Multiple Inheritance](task_04_flyingfish.py)**

## Background:
In some object-oriented languages, a class can inherit attributes and behaviors from more than one parent class. This is known as multiple inheritance. Python is one of the languages that supports multiple inheritance, which can be a powerful tool, but it also comes with complexities, particularly regarding method resolution order (MRO).

## Objective:
Construct a ```FlyingFish``` class that inherits from both a ```Fish``` class and a ```Bird``` class. Within ```FlyingFish```, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order.

## Instructions:
1. **Parent Classes Setup**:
* Create a ```Fish``` class with methods ```swim``` (which prints "The fish is swimming") and ```habitat``` (which prints "The fish lives in water").
* Create a ```Bird``` class with methods ```fly``` (which prints "The bird is flying") and ```habitat``` (which prints "The bird lives in the sky").
1. **Implementing FlyingFish**:
* Construct a ```FlyingFish``` class that inherits from both ```Fish``` and ```Bird```.
* Override the ```fly``` method to print "The flying fish is soaring!".
* Override the ```swim``` method to print "The flying fish is swimming!".
* Override the ```habitat``` method to print "The flying fish lives both in water and the sky!".
1. **Testing and MRO Exploration**:
* Instantiate an object of the ```FlyingFish``` class.
* Call the ```fly```, ```swim```, and ```habitat``` methods and observe the outputs.
* Use the ```mro()``` method or the .```__mro__``` attribute on the ```FlyingFish``` class to investigate the method resolution order. For instance, ```print(FlyingFish.mro())```.

<details>
<summary>Show answer</summary>

```python
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

```
</details>

---


* ## **[5. The Mystical Dragon - Mastering Mixins](task_05_dragon.py)**

## Background:
Mixins are a way to add functionality to classes in a modular fashion. They're not meant to stand alone but are meant to be combined with other classes to add behaviors. By using mixins, you can compose behaviors in classes without the need for deep or rigid inheritance hierarchies.

## Objective:
Design two mixin classes, ```SwimMixin``` and ```FlyMixin```, each equipped with methods ```swim``` and ```fly``` respectively. Next, construct a class ```Dragon``` that inherits from both these mixins. Your aim is to show that a ```Dragon``` instance can both swim and fly.

## Instructions:
1. **Creating Mixins**:
* Design a mixin called ```SwimMixin``` with a method ```swim``` that prints "The creature swims!".
* Design another mixin called ```FlyMixin``` with a method ```fly``` that prints "The creature flies!".
1. **Implementing Dragon**:
* Construct a class named ```Dragon``` that inherits from both ```SwimMixin``` and ```FlyMixin```.
* Within the ```Dragon``` class, you can add additional methods or attributes if desired, such as ```roar```, which could print "The dragon roars!".
1. **Testing the Dragon's Abilities**:
* Instantiate an object of the ```Dragon``` class named ```draco```.
* Demonstrate ```draco```'s abilities by calling the ```swim```, ```fly```, and (if implemented) ```roar``` methods.

<details>
<summary>Show answer</summary>

```python
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
```
</details>

---

  ### By Anthony Goutieras
  Weekly project from 02/02/26 to 06/02/26 for Holberton School Bordeaux
