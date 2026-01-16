<a href="#"><img src="https://img.shields.io/badge/-006CAF.svg?style=for-the-badge&logo=c&logoColor=white" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# Python - Hello, World
* ## **[0. Hello, print](2-print.py)**

Write a Python script that prints exactly ```"Programming is like building a multilingual puzzle```, followed by a new line.

* Use the function ```print```

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
```
</details>

---

* ## **[1. Print integer](3-print_number.py)**

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable ```number```, followed by ```Battery street```, followed by a new line.

  * You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/3-print_number.py)
  * The output of the script should be:

    * the number, followed by ```Battery street```,
    * followed by a new line
  * You are not allowed to cast the variable ```number``` into a string
  * Your code must be 3 lines long
  * You have to use f-strings [tips](https://intranet.hbtn.io/rltoken/dd7bIKsC3_0wb3Np_8URUA)

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
```
</details>

---
* ## **[2. Print float](4-print_float.py)**

Complete the source code in order to print the float stored in the variable ```number``` with a precision of 2 digits.

  * You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/4-print_float.py)
  * The output of the program should be:

    * ```Float:```, followed by the float with only 2 digits
    * followed by a new line
  * You are not allowed to cast ```number``` to string
  * You have to use f-strings

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
```
</details>

---
* ## **[3. Print string](5-print_string.py)**

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable ```str```, followed by its first 9 characters.

  * You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/5-print_string.py)
  * The output of the program should be:

    * 3 times the value of ```str```
    * followed by a new line
    * followed by the 9 first characters of ```str```
    * followed by a new line
  * You are not allowed to use any loops or conditional statement
  * Your program should be maximum 5 lines long

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
```
</details>

---
* ## **[4. Play with strings](6-concat.py)**

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/6-concat.py) to print ```Welcome to Holberton School!```

  * You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/6-concat.py)
  * You are not allowed to use any loops or conditional statements.
  * You have to use the variables ```str1``` and ```str2``` in your new line of code
  * Your program should be exactly 5 lines long

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = str1 + " " + str2
print(f"Welcome to {str1}!")
```
</details>

---
* ## **[5. Copy - Cut - Paste](7-edges.py)**

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/7-edges.py)

  * You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/7-edges.py)
  * You are not allowed to use any loops or conditional statements
  * Your program should be exactly 8 lines long
  * ```word_first_3``` should contain the first 3 letters of the variable ```word```
  * ```word_last_2``` should contain the last 2 letters of the variable ```word```
  * ```middle_word``` should contain the value of the variable ```word``` without the first and last letters

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
```
</details>

---
* ## **[6. Create a new sentence](8-concat_edges.py)**

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/8-concat_edges.py) to print ```object-oriented programming with Python```, followed by a new line.

  * You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/8-concat_edges.py)
  * You are not allowed to use any loops or conditional statements
  * Your program should be exactly 5 lines long
  * You are not allowed to create new variables
  * You are not allowed to use string literals

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
       language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[:6]
print(str)
```
</details>

---
* ## **[7. Easter Egg](6-easter_egg.py)**

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

  * Your script should be maximum 98 characters long (please check with ```wc -m 9-easter_egg.py```)

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
import this
```
</details>

---
  ### By Anthony Goutieras
  Weekly project from 12/01/26 to 16/01/26 for Holberton School Bordeaux
