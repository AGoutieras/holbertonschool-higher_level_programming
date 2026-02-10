<a href="#"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# Python - More Classes and Objects

* ## **[0. Simple rectangle](0-rectangle.py)**

Write an empty class ```Rectangle``` that defines a rectangle:

* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a rectangle."""


class Rectangle:
    """Represents a rectangle."""
    pass
```
</details>

---

* ## **[1. Real definition of a rectangle](1-rectangle.py)**

Write a class ```Rectangle``` that defines a rectangle by: (based on ```0-rectangle.py```)

* Private instance attribute: ```width```:
  * property ```def width(self):``` to retrieve it
  * property setter ```def width(self, value):``` to set it:
    * ```width``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```width must be an integer```
    * if ```width``` is less than ```0```, raise a ```ValueError``` exception with the message ```width must be >= 0```
* Private instance attribute: ```height```:
  * property ```def height(self):``` to retrieve it
  * property setter ```def height(self, value):``` to set it:
    * ```height``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```height must be an integer```
    * if ```height``` is less than ```0```, raise a ```ValueError``` exception with the message ```height must be >= 0```
* Instantiation with optional ```width``` and ```height```: ```def __init__(self, width=0, height=0):```
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle (must be >= 0).
        height (int): The height of the rectangle (must be >= 0).
    """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Optional, width of the rectangle (default 0).
            height (int): Optional, height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
```
</details>

---

* ## **[2. Area and Perimeter](2-rectangle.py)**

Write a class ```Rectangle``` that defines a rectangle by: (based on ```1-rectangle.py```)

* Private instance attribute: ```width```:
  * property ```def width(self):``` to retrieve it
  * property setter ```def width(self, value):``` to set it:
    * ```width``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```width must be an integer```
    * if ```width``` is less than ```0```, raise a ```ValueError``` exception with the message ```width must be >= 0```
* Private instance attribute: ```height```:
  * property ```def height(self):``` to retrieve it
  * property setter ```def height(self, value):``` to set it:
    * ```height``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```height must be an integer```
    * if ```height``` is less than ```0```, raise a ```ValueError``` exception with the message ```height must be >= 0```
* Instantiation with optional ```width``` and ```height```: ```def __init__(self, width=0, height=0):```
* Public instance method: ```def area(self):``` that returns the rectangle area
* Public instance method: ```def perimeter(self):``` that returns the rectangle perimeter:
  * if ```width``` or ```height``` is equal to ```0```, perimeter is equal to ```0```
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle (must be >= 0).
        height (int): The height of the rectangle (must be >= 0).
    """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Optional, width of the rectangle (default 0).
            height (int): Optional, height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
```
</details>

---

* ## **[3. String representation](3-rectangle.py)**

Write a class ```Rectangle``` that defines a rectangle by: (based on ```2-rectangle.py```)

* Private instance attribute: ```width```:
  * property ```def width(self):``` to retrieve it
  * property setter ```def width(self, value):``` to set it:
    * ```width``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```width must be an integer```
    * if ```width``` is less than ```0```, raise a ```ValueError``` exception with the message ```width must be >= 0```
* Private instance attribute: ```height```:
  * property ```def height(self):``` to retrieve it
  * property setter ```def height(self, value):``` to set it:
    * ```height``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```height must be an integer```
    * if ```height``` is less than ```0```, raise a ```ValueError``` exception with the message ```height must be >= 0```
* Instantiation with optional ```width``` and ```height```: ```def __init__(self, width=0, height=0):```
* Public instance method: ```def area(self):``` that returns the rectangle area
* Public instance method: ```def perimeter(self):``` that returns the rectangle perimeter:
  * if ```width``` or ```height``` is equal to ```0```, perimeter is equal to ```0```
* ```print()``` and ```str()``` should print the rectangle with the character ```#```
  * if ```width``` or ```height``` is equal to 0, return an empty string
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle (must be >= 0).
        height (int): The height of the rectangle (must be >= 0).
    """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Optional, width of the rectangle (default 0).
            height (int): Optional, height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Each line contains 'width' number of '#' characters, and the total
        number of lines is 'height'.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []

        for line in range(self.__height):
            lines.append("#" * self.__width)

        return f"\n".join(lines)
```
</details>

---

* ## **[4. Eval is magic](4-rectangle.py)**

Write a class ```Rectangle``` that defines a rectangle by: (based on ```3-rectangle.py```)

* Private instance attribute: ```width```:
  * property ```def width(self):``` to retrieve it
  * property setter ```def width(self, value):``` to set it:
    * ```width``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```width must be an integer```
    * if ```width``` is less than ```0```, raise a ```ValueError``` exception with the message ```width must be >= 0```
* Private instance attribute: ```height```:
  * property ```def height(self):``` to retrieve it
  * property setter ```def height(self, value):``` to set it:
    * ```height``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```height must be an integer```
    * if ```height``` is less than ```0```, raise a ```ValueError``` exception with the message ```height must be >= 0```
* Instantiation with optional ```width``` and ```height```: ```def __init__(self, width=0, height=0):```
* Public instance method: ```def area(self):``` that returns the rectangle area
* Public instance method: ```def perimeter(self):``` that returns the rectangle perimeter:
  * if ```width``` or ```height``` is equal to ```0```, perimeter is equal to ```0```
* ```print()``` and ```str()``` should print the rectangle with the character ```#```
  * if ```width``` or ```height``` is equal to 0, return an empty string
* ```repr()``` should return a string representation of the rectangle to be able to recreate a new instance by using ```eval()```
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle (must be >= 0).
        height (int): The height of the rectangle (must be >= 0).
    """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Optional, width of the rectangle (default 0).
            height (int): Optional, height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Each line contains 'width' number of '#' characters, and the total
        number of lines is 'height'.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []

        for line in range(self.__height):
            lines.append("#" * self.__width)

        return f"\n".join(lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate a new instance with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"
```
</details>

---

* ## **[5. Detect instance deletion](5-rectangle.py)**

Write a class ```Rectangle``` that defines a rectangle by: (based on ```4-rectangle.py```)

* Private instance attribute: ```width```:
  * property ```def width(self):``` to retrieve it
  * property setter ```def width(self, value):``` to set it:
    * ```width``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```width must be an integer```
    * if ```width``` is less than ```0```, raise a ```ValueError``` exception with the message ```width must be >= 0```
* Private instance attribute: ```height```:
  * property ```def height(self):``` to retrieve it
  * property setter ```def height(self, value):``` to set it:
    * ```height``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```height must be an integer```
    * if ```height``` is less than ```0```, raise a ```ValueError``` exception with the message ```height must be >= 0```
* Instantiation with optional ```width``` and ```height```: ```def __init__(self, width=0, height=0):```
* Public instance method: ```def area(self):``` that returns the rectangle area
* Public instance method: ```def perimeter(self):``` that returns the rectangle perimeter:
  * if ```width``` or ```height``` is equal to ```0```, perimeter is equal to ```0```
* ```print()``` and ```str()``` should print the rectangle with the character ```#```
  * if ```width``` or ```height``` is equal to 0, return an empty string
* ```repr()``` should return a string representation of the rectangle to be able to recreate a new instance by using ```eval()```
* Print the message ```Bye rectangle...``` (```...``` being 3 dots not ellipsis) when an instance of ```Rectangle``` is deleted
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle (must be >= 0).
        height (int): The height of the rectangle (must be >= 0).
    """
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Optional, width of the rectangle (default 0).
            height (int): Optional, height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Each line contains 'width' number of '#' characters, and the total
        number of lines is 'height'.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []

        for line in range(self.__height):
            lines.append("#" * self.__width)

        return f"\n".join(lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate a new instance with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message on deletion"""
        print("Bye rectangle...")
```
</details>

---

* ## **[6. How many instances](6-rectangle.py)**

Write a class ```Rectangle``` that defines a rectangle by: (based on ```4-rectangle.py```)

* Private instance attribute: ```width```:
  * property ```def width(self):``` to retrieve it
  * property setter ```def width(self, value):``` to set it:
    * ```width``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```width must be an integer```
    * if ```width``` is less than ```0```, raise a ```ValueError``` exception with the message ```width must be >= 0```
* Private instance attribute: ```height```:
  * property ```def height(self):``` to retrieve it
  * property setter ```def height(self, value):``` to set it:
    * ```height``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```height must be an integer```
    * if ```height``` is less than ```0```, raise a ```ValueError``` exception with the message ```height must be >= 0```
* Public class attribute ```number_of_instances```:
  * Initialized to ```0```
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Instantiation with optional ```width``` and ```height```: ```def __init__(self, width=0, height=0):```
* Public instance method: ```def area(self):``` that returns the rectangle area
* Public instance method: ```def perimeter(self):``` that returns the rectangle perimeter:
  * if ```width``` or ```height``` is equal to ```0```, perimeter is equal to ```0```
* ```print()``` and ```str()``` should print the rectangle with the character ```#```
  * if ```width``` or ```height``` is equal to 0, return an empty string
* ```repr()``` should return a string representation of the rectangle to be able to recreate a new instance by using ```eval()```
* Print the message ```Bye rectangle...``` (```...``` being 3 dots not ellipsis) when an instance of ```Rectangle``` is deleted
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle (must be >= 0).
        height (int): The height of the rectangle (must be >= 0).
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Optional, width of the rectangle (default 0).
            height (int): Optional, height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Each line contains 'width' number of '#' characters, and the total
        number of lines is 'height'.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []

        for line in range(self.__height):
            lines.append("#" * self.__width)

        return f"\n".join(lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate a new instance with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message on deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
```
</details>

---

* ## **[7. Change representation](7-rectangle.py)**

Write a class ```Rectangle``` that defines a rectangle by: (based on ```4-rectangle.py```)

* Private instance attribute: ```width```:
  * property ```def width(self):``` to retrieve it
  * property setter ```def width(self, value):``` to set it:
    * ```width``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```width must be an integer```
    * if ```width``` is less than ```0```, raise a ```ValueError``` exception with the message ```width must be >= 0```
* Private instance attribute: ```height```:
  * property ```def height(self):``` to retrieve it
  * property setter ```def height(self, value):``` to set it:
    * ```height``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```height must be an integer```
    * if ```height``` is less than ```0```, raise a ```ValueError``` exception with the message ```height must be >= 0```
* Public class attribute ```number_of_instances```:
  * Initialized to ```0```
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class ```attribute print_symbol```:
  * Initialized to ```#```
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional ```width``` and ```height```: ```def __init__(self, width=0, height=0):```
* Public instance method: ```def area(self):``` that returns the rectangle area
* Public instance method: ```def perimeter(self):``` that returns the rectangle perimeter:
  * if ```width``` or ```height``` is equal to ```0```, perimeter is equal to ```0```
* ```print()``` and ```str()``` should print the rectangle with the character(s) stored in ```print_symbol```:
  * if ```width``` or ```height``` is equal to 0, return an empty string
* ```repr()``` should return a string representation of the rectangle to be able to recreate a new instance by using ```eval()```
* Print the message ```Bye rectangle...``` (```...``` being 3 dots not ellipsis) when an instance of ```Rectangle``` is deleted
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle (must be >= 0).
        height (int): The height of the rectangle (must be >= 0).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Optional, width of the rectangle (default 0).
            height (int): Optional, height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Each line contains 'width' number of '#' characters, and the total
        number of lines is 'height'.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []

        for line in range(self.__height):
            lines.append(str(self.print_symbol) * self.__width)

        return f"\n".join(lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate a new instance with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message on deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
```
</details>

---

* ## **[8. Compare rectangles](8-rectangle.py)**

Write a class ```Rectangle``` that defines a rectangle by: (based on ```4-rectangle.py```)

* Private instance attribute: ```width```:
  * property ```def width(self):``` to retrieve it
  * property setter ```def width(self, value):``` to set it:
    * ```width``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```width must be an integer```
    * if ```width``` is less than ```0```, raise a ```ValueError``` exception with the message ```width must be >= 0```
* Private instance attribute: ```height```:
  * property ```def height(self):``` to retrieve it
  * property setter ```def height(self, value):``` to set it:
    * ```height``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```height must be an integer```
    * if ```height``` is less than ```0```, raise a ```ValueError``` exception with the message ```height must be >= 0```
* Public class attribute ```number_of_instances```:
  * Initialized to ```0```
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class ```attribute print_symbol```:
  * Initialized to ```#```
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional ```width``` and ```height```: ```def __init__(self, width=0, height=0):```
* Public instance method: ```def area(self):``` that returns the rectangle area
* Public instance method: ```def perimeter(self):``` that returns the rectangle perimeter:
  * if ```width``` or ```height``` is equal to ```0```, perimeter is equal to ```0```
* ```print()``` and ```str()``` should print the rectangle with the character ```#```:
  * if ```width``` or ```height``` is equal to 0, return an empty string
* ```repr()``` should return a string representation of the rectangle to be able to recreate a new instance by using ```eval()```
* Print the message ```Bye rectangle...``` (```...``` being 3 dots not ellipsis) when an instance of ```Rectangle``` is deleted
* Static method ```def bigger_or_equal(rect_1, rect_2):``` that returns the biggest rectangle based on the area
  * ```rect_1``` must be an instance of Rectangle, otherwise raise a ```TypeError``` exception with the message ```rect_1 must be an instance of Rectangle```
  * ```rect_2``` must be an instance of Rectangle, otherwise raise a ```TypeError``` exception with the message ```rect_2 must be an instance of Rectangle```
  * Returns ```rect_1``` if both have the same area value
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle (must be >= 0).
        height (int): The height of the rectangle (must be >= 0).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Optional, width of the rectangle (default 0).
            height (int): Optional, height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area, or rect_1 if equal.

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        else:
            return rect_2

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Each line contains 'width' number of '#' characters, and the total
        number of lines is 'height'.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []

        for line in range(self.__height):
            lines.append(str(self.print_symbol) * self.__width)

        return f"\n".join(lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate a new instance with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message on deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
```
</details>

---

* ## **[9. A square is a rectangle](9-rectangle.py)**

Write a class ```Rectangle``` that defines a rectangle by: (based on ```4-rectangle.py```)

* Private instance attribute: ```width```:
  * property ```def width(self):``` to retrieve it
  * property setter ```def width(self, value):``` to set it:
    * ```width``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```width must be an integer```
    * if ```width``` is less than ```0```, raise a ```ValueError``` exception with the message ```width must be >= 0```
* Private instance attribute: ```height```:
  * property ```def height(self):``` to retrieve it
  * property setter ```def height(self, value):``` to set it:
    * ```height``` must be an integer, otherwise raise a ```TypeError``` exception with the message ```height must be an integer```
    * if ```height``` is less than ```0```, raise a ```ValueError``` exception with the message ```height must be >= 0```
* Public class attribute ```number_of_instances```:
  * Initialized to ```0```
  * Incremented during each new instance instantiation
  * Decremented during each instance deletion
* Public class ```attribute print_symbol```:
  * Initialized to ```#```
  * Used as symbol for string representation
  * Can be any type
* Instantiation with optional ```width``` and ```height```: ```def __init__(self, width=0, height=0):```
* Public instance method: ```def area(self):``` that returns the rectangle area
* Public instance method: ```def perimeter(self):``` that returns the rectangle perimeter:
  * if ```width``` or ```height``` is equal to ```0```, perimeter is equal to ```0```
* ```print()``` and ```str()``` should print the rectangle with the character ```#```:
  * if ```width``` or ```height``` is equal to 0, return an empty string
* ```repr()``` should return a string representation of the rectangle to be able to recreate a new instance by using ```eval()```
* Print the message ```Bye rectangle...``` (```...``` being 3 dots not ellipsis) when an instance of ```Rectangle``` is deleted
* Static method ```def bigger_or_equal(rect_1, rect_2):``` that returns the biggest rectangle based on the area
  * ```rect_1``` must be an instance of Rectangle, otherwise raise a ```TypeError``` exception with the message ```rect_1 must be an instance of Rectangle```
  * ```rect_2``` must be an instance of Rectangle, otherwise raise a ```TypeError``` exception with the message ```rect_2 must be an instance of Rectangle```
  * Returns ```rect_1``` if both have the same area value
* Class method ```def square(cls, size=0):``` that returns a new Rectangle instance with ```width == height == size```
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
"""Defines a rectangle class with width and height attributes."""


class Rectangle:
    """Represents a rectangle with width and height.

    Attributes:
        width (int): The width of the rectangle (must be >= 0).
        height (int): The height of the rectangle (must be >= 0).
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): Optional, width of the rectangle (default 0).
            height (int): Optional, height of the rectangle (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height, ensuring it is an int >= 0."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the greater area, or rect_1 if equal.

        Raises:
            TypeError: If rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        return cls(size, size)

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """
        Return the perimeter of the rectangle.

        If width or height is 0, returns 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Return a string representation of the rectangle using '#' characters.

        Each line contains 'width' number of '#' characters, and the total
        number of lines is 'height'.
        If width or height is 0, returns an empty string.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lines = []

        for line in range(self.__height):
            lines.append(str(self.print_symbol) * self.__width)

        return f"\n".join(lines)

    def __repr__(self):
        """
        Return a string representation of the rectangle
        that can be used to recreate a new instance with eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message on deletion"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
```
</details>

---

  ### By Anthony Goutieras
  Weekly project from 26/01/26 to 30/01/26 for Holberton School Bordeaux
