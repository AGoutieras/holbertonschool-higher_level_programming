<a href="#"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# Python - Inheritance

* ## **[0. Lookup](0-lookup.py)**

Write a function that returns the list of available attributes and methods of an object:

  * Prototype: `def lookup(obj):`
  * Returns a `list` object
  * You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Function that returns the list of attributes and methods of an object"""


def lookup(obj):
    """Return a list of available attributes and methods of obj"""
    return dir(obj)
```
</details>

---

* ## **[1. My list](1-my_list.py)**

Write a class `MyList` that inherits from `list`:

  * Public instance method: `def print_sorted(self):` that prints the list, but sorted (ascending sort)
  * You can assume that all the elements of the list will be of type `int`
  * You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""
Define an inherited list class MyList
"""


class MyList(list):
    """
    Inherit from list and add a print_sorted method
    """
    def print_sorted(self):
        """
        Print the list in ascending order
        """
        print(sorted(self))
```
</details>

---

* ## **[2. Exact same object](2-is_same_class.py)**

Write a function that returns `True` if the object is exactly an instance of the specified class ; otherwise `False`.

  * Prototype: `def is_same_class(obj, a_class):`
  * You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Check if an object is exactly an instance of a given class"""


def is_same_class(obj, a_class):
    """
    Return True if obj is an instance of a_class

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare the object against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
```
</details>

---

* ## **[3. Same class or inherit from](3-is_kind_of_class.py)**

Write a function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise `False`.

  * Prototype: `def is_kind_of_class(obj, a_class):`
  * You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Check if an object is an instance or inherited instance of a given class"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance or inherited instance of a_class"""
    if isinstance(obj, a_class):
        return True
    return False
```
</details>

---

* ## **[4. Only sub class of](4-inherits_from.py)**

Write a function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise `False`.

  * Prototype: `def inherits_from(obj, a_class):`
  * You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Check if an object is an inherited instance of a given class"""


def inherits_from(obj, a_class):
    """Check if an object is an inherited instance of a given class"""
    return False if type(obj) is a_class else issubclass(type(obj), a_class)
```
</details>

---

* ## **[5. Geometry module](5-base_geometry.py)**

Write an empty class `BaseGeometry`.

  * You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Define an empty class 'BaseGeometry'"""


class BaseGeometry:
    """Represents BaseGeometry"""
    pass
```
</details>

---

* ## **[6. Improve Geometry](6-base_geometry.py)**

Write a class `BaseGeometry` (based on `5-base_geometry.py`).

  * Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
  * You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Define a base geometry class 'BaseGeometry'"""


class BaseGeometry:
    """Represents BaseGeometry"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")
```
</details>

---

* ## **[7. Integer validator](7-base_geometry.py)**

Write a class `BaseGeometry` (based on `6-base_geometry.py`).

  * Public instance method: `def area(self):` that raises an `Exception` with the message `area() is not implemented`
  * Public instance method: `def integer_validator(self, name, value):` that validates `value`:
  * you can assume `name` is always a string
  * if `value` is not an integer: raise a `TypeError` exception, with the message `<name> must be an integer`
  * if `value` is less or equal to 0: raise a `ValueError` exception with the message `<name> must be greater than 0`
  * You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Define a base geometry class 'BaseGeometry'"""


class BaseGeometry:
    """Represents BaseGeometry"""
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Checks if value is an int and is greater than 0"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
```
</details>

---

* ## **[8. Rectangle](8-rectangle.py)**

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`).

  * Instantiation with `width` and `height`: `def __init__(self, width, height):`
  * `width` and `height` must be private. No getter or setter
  * `width` and `height` must be positive integers, validated by `integer_validator`

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Define a base geometry class 'BaseGeometry'"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Initialize rectangle with validated width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
```
</details>

---

* ## **[9. Full rectangle](9-rectangle.py)**

Write a class `Rectangle` that inherits from `BaseGeometry` (`7-base_geometry.py`). (task based on `8-rectangle.py`)

  * Instantiation with `width` and `height`: `def __init__(self, width, height):`:
  * `width` and `height` must be private. No getter or setter
  * `width` and `height` must be positive integers validated by `integer_validator`
  * the `area()` method must be implemented
  * `print()` should print, and `str()` should return, the following rectangle description: `[Rectangle] <width>/<height>`

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Define a base geometry class 'BaseGeometry'"""


class BaseGeometry:
    """Represents BaseGeometry"""
    def integer_validator(self, name, value):
        """Checks if value is an int and is greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Initialize rectangle with validated width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
```
</details>

---

* ## **[10. Square #1](10-square.py)**

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`):

  * Instantiation with `size`: `def __init__(self, size):`:
  * `size` must be private. No getter or setter
  * `size` must be a positive integer, validated by `integer_validator`
  * the `area()` method must be implemented

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Define a base geometry class 'BaseGeometry'"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """Initializes a Square instance."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
```
</details>

---

* ## **[11. Square #2](11-square.py)**

Write a class `Square` that inherits from `Rectangle` (`9-rectangle.py`). (task based on `10-square.py`).

  * Instantiation with size: `def __init__(self, size):`:
  * `size` must be private. No getter or setter
  * `size` must be a positive integer, validated by `integer_validator`
  * the `area()` method must be implemented
  * `print()` should print, and `str()` should return, the square description: `[Square] <width>/<height>`

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
"""Define a base geometry class 'BaseGeometry'"""


class BaseGeometry:
    """Represents BaseGeometry"""
    def integer_validator(self, name, value):
        """Checks if value is an int and is greater than 0"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Represents a rectangle"""
    def __init__(self, width, height):
        """Initialize rectangle with validated width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size):
        """Initializes a Square instance."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """Return the string representation of the square"""
        return f"[Square] {self.__size}/{self.__size}"
```
</details>

---

  ### By Anthony Goutieras
  Weekly project from 02/02/26 to 06/02/26 for Holberton School Bordeaux
