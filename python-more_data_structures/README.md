<a href="#"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# Python - More Data Structures: Set, Dictionary

* ## **[0. Squared simple](0-square_matrix_simple.py)**

Write a function that computes the square value of all integers of a matrix.

* Prototype: ```def square_matrix_simple(matrix=[]):```
* ```matrix``` is a 2 dimensional array
* Returns a new matrix:
  * Same size as ```matrix```
  * Each value should be the square of the value of the input
* Initial matrix should not be modified
* You are not allowed to import any module
* You are allowed to use regular loops, ```map```, etc.

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            new_row.append(matrix[i][j] ** 2)
        new_matrix.append(new_row)

    return new_matrix
```
</details>

---

* ## **[1. Search and replace](1-search_replace.py)**

Write a function that replaces all occurrences of an element by another in a new list.

* Prototype: ```def search_replace(my_list, search, replace):```
* ```my_list``` is the initial list
* ```search``` is the element to replace in the list
* ```replace``` is the new element
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []

    for elem in my_list:
        if elem == search:
            new_list.append(replace)
        else:
            new_list.append(elem)

    return (new_list)
```
</details>

---

* ## **[2. Unique addition](2-uniq_add.py)**

Write a function that adds all unique integers in a list (only once for each integer).

* Prototype: ```def uniq_add(my_list=[]):```
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def uniq_add(my_list=[]):

    total = 0
    seen = []
    for num in my_list:
        if num not in seen:
            total += num
            seen.append(num)

    return total
```
</details>

---

* ## **[3. Present in both](3-common_elements.py)**

Write a function that returns a set of common elements in two sets.

* Prototype: ```def common_elements(set_1, set_2):```
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []

    for i in set_1:
        if i in set_2:
            common.append(i)

    return common
```
</details>

---

* ## **[4. Only differents](4-only_diff_elements.py)**

Write a function that returns a set of all elements present in only one set.

* Prototype: ```def only_diff_elements(set_1, set_2):```
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def only_diff_elements(set_1, set_2):

    diff = []

    for i in set_1:
        if i not in set_2:
            diff.append(i)

    for i in set_2:
        if i not in set_1:
            diff.append(i)

    return diff
```
</details>

---

* ## **[5. Number of keys](5-number_keys.py)**

Write a function that returns the number of keys in a dictionary.

* Prototype: ```def number_keys(a_dictionary):```
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def number_keys(a_dictionary):
    return len(a_dictionary)
```
</details>

---

* ## **[6. Print sorted dictionary](6-print_sorted_dictionary.py)**

Write a function that prints a dictionary by ordered keys.

* Prototype: ```def print_sorted_dictionary(a_dictionary):```
* You can assume that all keys are strings
* Keys should be sorted by alphabetic order
* Only sort keys of the first level (don’t sort keys of a dictionary inside the main dictionary)
* Dictionary values can have any type
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary.keys()):
        print("{}: {}".format(i, a_dictionary[i]))
```
</details>

---

* ## **[7. Update dictionary](7. Update dictionary)**

Write a function that replaces or adds key/value in a dictionary.

* Prototype: ```def update_dictionary(a_dictionary, key, value):```
* ```key``` argument will be always a string
* ```value``` argument will be any type
* If a key exists in the dictionary, the value will be replaced
* If a key doesn’t exist in the dictionary, it will be created
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
```
</details>

---

* ## **[8. Simple delete by key](8-simple_delete.py)**

Write a function that deletes a key in a dictionary.

* Prototype: ```def simple_delete(a_dictionary, key=""):```
* ```key``` argument will be always a string
* If a key doesn’t exist, the dictionary won’t change
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
```
</details>

---

* ## **[9. Multiply by 2](9-multiply_by_2.py)**

Write a function that returns a new dictionary with all values multiplied by 2

* Prototype: ```def multiply_by_2(a_dictionary):```
* You can assume that all values are only integers
* Returns a new dictionary
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}

    for key, value in a_dictionary.items():
        new_dict[key] = value * 2

    return new_dict
```
</details>

---

* ## **[10. Best score](10-best_score.py)**

Write a function that returns a key with the biggest integer value.

* Prototype: ```def best_score(a_dictionary):```
* You can assume that all values are only integers
* If no score found, return ```None```
* You can assume all students have a different score
* You are not allowed to import any module

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    max_value = 0
    max_key = 0

    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key

    return max_key
```
</details>

---

* ## **[11. Multiply by using map](11-multiply_list_map.py)**

Write a function that returns a list with all values multiplied by a number without using any loops.

* Prototype: ```def multiply_list_map(my_list=[], number=0):```
* Returns a new list:
  * Same length as ```my_list```
  * Each value should be multiplied by ```number```
* Initial list should not be modified
* You are not allowed to import any module
* You have to use ```map```
* Your file should be max 3 lines

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
```
</details>

---

* ## **[12. Roman to Integer](12-roman_to_int.py)**

**Technical interview preparation:**

* You are not allowed to google anything
* Whiteboard first

Create a function )```def roman_to_int(roman_string):)``` that converts a [Roman numeral](https://en.wikipedia.org/wiki/Roman_numerals) to an integer.

* You can assume the number will be between 1 to 3999.
* ```def roman_to_int(roman_string)``` must return an integer
* If the ```roman_string``` is not a string or ```None```, return 0

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == "":
        return 0

    total = 0
    i = 0

    rmn_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    while i < len(roman_string):
        value = rmn_dict[roman_string[i]]

        if i + 1 < len(roman_string) and rmn_dict[roman_string[i + 1]] > value:
            total += rmn_dict[roman_string[i + 1]] - value
            i += 2

        else:
            total += value
            i += 1

    return total
```
</details>

---

  ### By Anthony Goutieras
  Weekly project from 19/01/26 to 23/01/26 for Holberton School Bordeaux
