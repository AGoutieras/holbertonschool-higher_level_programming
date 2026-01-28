<a href="#"><img src="https://img.shields.io/badge/-006CAF.svg?style=for-the-badge&logo=c&logoColor=white" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# Python - Classes and Objects

* ## **[0. My first square](0-square.py)**

Write an empty class ```Square``` that defines a square:

* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""
    pass
```
</details>

---

* ## **[1. Square with size](1-square.py)**

Write a class ```Square``` that defines a square by: (based on ```0-square.py```)

* Private instance attribute: ```size```
* Instantiation with ```size``` (no type/value verification)
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""
    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size: The size of the square.
        """
        self.__size = size
```
</details>

---


* ## **[2. Size validation](2-square.py)**

Write a class ```Square``` that defines a square by: (based on ```1-square.py```)

* Private instance attribute: ```size```
* Instantiation with optional ```size```: ```def __init__(self, size=0):```
  * ```size``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
  * if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square. Must be >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
```
</details>

---


* ## **[3. Area of a square](3-square.py)**

Write a class ```Square``` that defines a square by: (based on ```2-square.py```)

Private instance attribute: ```size```
Instantiation with optional ```size```: ```def __init__(self, size=0):```
```size``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
Public instance method: ```def area(self):``` that returns the current square area
You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square. Must be >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
```
</details>

---


* ## **[4. Access and update private attribute](4-square.py)**

Write a class ```Square``` that defines a square by: (based on ```3-square.py```)

* Private instance attribute: ```size```:
  * property ```def size(self):``` to retrieve it
  * property setter ```def size(self, value):``` to set it:
    * ```size``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
    * if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
* Instantiation with optional ```size```: ```def __init__(self, size=0):```
* Public instance method: ```def area(self):``` that returns the current square area
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (private).

    Properties:
        size (int): Getter and setter for the square's size with validation.
                     Must be an integer >= 0.

    Methods:
        area(): Returns the current square area.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square. Must be >= 0.
                                  Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.size = size

    @property
    def size(self):
        """
        Getter for the square's size.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the square's size with validation.

        Args:
            value (int): The new size of the square. Must be >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2
```
</details>

---

* ## **[5. Printing a square](5-square.py)**

Write a class ```Square``` that defines a square by: (based on ```4-square.py```)

* Private instance attribute: ```size```:
  * property ```def size(self):``` to retrieve it
  * property setter ```def size(self, value):``` to set it:
    * ```size``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
    * if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
* Instantiation with optional ```size```: ```def __init__(self, size=0):```
* Public instance method: ```def area(self):``` that returns the current square area
* Public instance method: ```def my_print(self):``` that prints in stdout the square with the character ```#```:
  * if ```size``` is equal to 0, print an empty line
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Represents a square with a private size attribute.

    Attributes:
        __size (int): The size of the square (private).

    Properties:
        size (int): Getter and setter for the square's size with validation.
                     Must be an integer >= 0.

    Methods:
        area(): Returns the current square area.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square. Must be >= 0.
                                  Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        self.size = size

    @property
    def size(self):
        """
        Getter for the square's size.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the square's size with validation.

        Args:
            value (int): The new size of the square. Must be >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.

        If the size of the square is 0, prints an empty line.
        """
        for line in range(self.__size):
            print("#" * self.__size)

        if self.__size == 0:
            print()
            return
```
</details>

---

* ## **[](6-square.py)**

Write a class ```Square``` that defines a square by: (based on ```4-square.py```)

* Private instance attribute: ```size```:
  * property ```def size(self):``` to retrieve it
  * property setter ```def size(self, value):``` to set it:
    * ```size``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```size must be an integer```
    * if ```size``` is less than ```0```, raise a ```ValueError``` exception with the message ```size must be >= 0```
* Private instance attribute: ```position```:
  * property ```def position(self):``` to retrieve it
  * property setter ```def position(self, value):``` to set it:
    * ```position``` must be a tuple of 2 positive integers, otherwise raise a ```TypeError``` exception with the message ```position must be a tuple of 2 positive integers```
* Instantiation with optional ```size``` and optional position: ```def __init__(self, size=0, position=(0, 0)):```
* Public instance method: ```def area(self):``` that returns the current square area
* Public instance method: ```def my_print(self):``` that prints in stdout the square with the character ```#```:
  * if ```size``` is equal to 0, print an empty line
  * ```position``` should be set using space - Don’t fill lines by spaces when ```position[1] > 0```
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a square."""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private, >= 0).
        __position (tuple): The position of the square.

    Properties:
        size (int): Getter and setter for the size with validation.
        position (tuple): Getter and setter for the position with validation.

    Methods:
        area(): Returns the current area of the square.
        my_print(): Prints the square using '#' considering position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance.

        Args:
            size (int, optional): The size of the square.
            position (tuple, optional): The position (x, y) of the square.

        Raises:
            TypeError: If size is not an integer
                       or position is not a tuple of 2 positive integers.
            ValueError: If size is less than 0.
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the square's size.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the square's size with validation.

        Args:
            value (int): The new size of the square. Must be >= 0.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter for the square's position.

        Returns:
            tuple: The current position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the square's position with validation.

        Args:
            value (tuple): A tuple of 2 positive integers representing (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if not len(value) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Computes the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character '#' to stdout.

        If the size is 0, prints an empty line.
        The position attribute controls the horizontal and vertical offset.
        """
        if self.__size == 0:
            print()
            return

        for line in range(self.__position[1]):
            print()

        for line in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
```
</details>

---

  ### By Anthony Goutieras
  Weekly project from 26/01/26 to 30/01/26 for Holberton School Bordeaux
