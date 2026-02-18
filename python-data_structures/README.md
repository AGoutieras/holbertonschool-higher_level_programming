<a href="#"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# Python - Data Structures: Lists, Tuples

* ## **[0. Print a list of integers](0-print_list_integer.py)**

Write a function that prints all integers of a list.

* Prototype: ```def print_list_integer(my_list=[]):```
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use ```str.format()``` to print integers

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for i in my_list:
        print("{:d}".format(i))

```
</details>

---

* ## **[1. Secure access to an element in a list](1-element_at.py)**

Write a function that retrieves an element from a list.

* Prototype: ```def element_at(my_list, idx):```
* If ```idx``` is negative, the function should return None
* If ```idx``` is out of range (> of number of element in ```my_list```), the function should return ```None```
* You are not allowed to import any module
* You are not allowed to use ```try/except```

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None

    if idx > (len(my_list) - 1):
        return None

    else:
        return my_list[idx]
```
</details>

---


* ## **[2. Replace element](2-replace_in_list.py)**

Write a function that replaces an element of a list at a specific position.

Prototype: ```def replace_in_list(my_list, idx, element):```
If ```idx``` is negative, the function should not modify anything, and returns the original list
If ```idx``` is out of range (> of number of element in ```my_list```), the function should not modify anything, and returns the original list
You are not allowed to import any module
You are not allowed to use ```try/except```

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element

    return my_list
```
</details>

---


* ## **[3. Print a list of integers... in reverse!](3-print_reversed_list_integer.py)**

Write a function that prints all integers of a list, in reverse order.

* Prototype: ```def print_reversed_list_integer(my_list=[]):```
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use ```str.format()``` to print integers

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in reversed(my_list):
        print("{:d}".format(i))
```
</details>

---


* ## **[4. Replace in a copy](4-new_in_list.py)**

Write a function that replaces an element in a list at a specific position without modifying the original list.

* Prototype: ```def new_in_list(my_list, idx, element):```
* If ```idx``` is negative, the function should return a copy of the original ```list```
* If ```idx``` is out of range (> of number of element in ```my_list```), the function should return a copy of the original ```list```
* You are not allowed to import any module
* You are not allowed to use ```try/except```

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list

    list_copy = [i for i in my_list]
    list_copy[idx] = element
    return list_copy
```
</details>

---


* ## **[5. Can you C me now?](5-no_c.py)**

Write a function that removes all characters c and C from a string.

* Prototype: ```def no_c(my_string):```
* The function should return the new string
* You are not allowed to import any module
* You are not allowed to use ```str.replace()```

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def no_c(my_string):
    string_copy = [x for x in my_string if x != 'c' and x != 'C']

    return ''.join(string_copy)
```
</details>

---


* ## **[6. Lists of lists = Matrix](6-print_matrix_integer.py)**

Write a function that prints a matrix of integers.

* Prototype: ```def print_matrix_integer(matrix=[[]]):```
* Format: see example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use ```str.format()``` to print integers

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")

            if j != (len(matrix[i]) - 1):
                print(" ", end="")
        print("")
```
</details>

---


* ## **[7. Tuples addition](7-add_tuple.py)**

Write a function that adds 2 tuples.

* Prototype: ```def add_tuple(tuple_a=(), tuple_b=()):```
* Returns a tuple with 2 integers:
  * The first element should be the addition of the first element of each argument
  * The second element should be the addition of the second element of each argument
* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value ```0``` for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    return a0 + b0, a1 + b1
```
</details>

---


* ## **[8. More returns!](8-multiple_returns.py)**

Write a function that returns a tuple with the length of a string and its first character.

* Prototype: ```def multiple_returns(sentence):```
* If the sentence is empty, the first character should be equal to ```None```
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def multiple_returns(sentence):

    if sentence == "":
        return len(sentence), None

    else:
        return len(sentence), sentence[0]
```
</details>

---


* ## **[9. Find the max](9-max_integer.py)**

Write a function that finds the biggest integer of a list.

* Prototype: ```def max_integer(my_list=[]):```
* If the list is empty, return ```None```
* You can assume that the list only contains integers
* You are not allowed to import any module
* You are not allowed to use the builtin ```max()```

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_value = my_list[0]

    for i in my_list:
        if i > max_value:
            max_value = i

    return max_value
```
</details>

---


* ## **[10. Only by 2](10-divisible_by_2.py)**

Write a function that finds all multiples of 2 in a list.

* Prototype: ```def divisible_by_2(my_list=[]):```
* Return a new list with ```True``` or ```False```, depending on whether the integer at the same position in the original list is a multiple of 2
* The new list should have the same size as the original list
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    result = []

    for x in my_list:
        if x % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
```
</details>

---


* ## **[11. Delete at](11-delete_at.py)**

Write a function that deletes the item at a specific position in a list.

Prototype: ```def delete_at(my_list=[], idx=0):```
If ```idx``` is negative or out of range, nothing change (returns the same list)
You are not allowed to use ```pop()```
You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]

    return my_list
```
</details>

---


* ## **[12. Switch](12-switch.py)**

Complete the source code in order to switch value of ```a``` and ```b```

* You can find the source code [here](https://github.com/hs-hq/0x03.py/blob/main/12-switch_py)
* Your code should be inserted where the comment is (line 4)
* Your program should be exactly 5 lines long

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
a = 89
b = 10
a, b = b, a
print("a={:d} - b={:d}".format(a, b))
```
</details>

---

  ### By Anthony Goutieras
  Weekly project from 19/01/26 to 23/01/26 for Holberton School Bordeaux
