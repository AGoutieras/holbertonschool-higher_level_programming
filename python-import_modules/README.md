<a href="#"><img src="https://img.shields.io/badge/-006CAF.svg?style=for-the-badge&logo=c&logoColor=white" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# Python - import & modules

## **[0. Import a simple function from a simple file](0-add.py)**

Write a program that imports the function ```def add(a, b):``` from the file ```add_0.py``` and prints the result of the addition ```1 + 2 = 3```

* You have to use ```print``` function with string format to display integers
* You have to assign:
    * the value ```1``` to a variable called ```a```
    * the value ```2``` to a variable called ```b```
    * and use those two variables as arguments when calling the functions ```add``` and ```print```
* ```a``` and ```b``` must be defined in 2 different lines: ```a = 1``` and another ```b = 2```
* Your program should print: ```<a value> + <b value> = <add(a, b) value>``` followed with a new line
* You can only use the word ```add_0``` once in your code
* You are not allowed to use ```*``` for importing or ```__import__```
* Your code should not be executed when imported - by using ```__import__```, like the example below
<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
```
</details>

---

## **[1. My first toolbox!](1-calculation.py)**

Write a program that imports functions from the file ```calculator_1.py```, does some Maths, and prints the result.

* Do not use the function ```print``` (with string format to display integers) more than 4 times
* You have to define:
    * the value ```10``` to a variable ```a```
    * the value ```5``` to a variable ```b```
    * and use those two variables only, as arguments when calling functions (including ```print```)
* ```a``` and ```b``` must be defined in 2 different lines: ```a = 10``` and another ```b = 5```
* Your program should call each of the imported functions. See example below for format
* the word ```calculator_1``` should be used only once in your file
* You are not allowed to use ```*``` for importing or ```__import__```
* Your code should not be executed when imported
<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
```
</details>

---

## **[2. How to make a script dynamic!](2-args.py)**

Write a program that prints the number of and the list of its arguments.

* The output should be:
    * Number of argument(s) followed by ```argument``` (if number is one) or ```arguments``` (otherwise), followed by
    * ```:``` (or ```.``` if no arguments were passed) followed by
    * a new line, followed by (if at least one argument),
    * one line per argument:
        * the position of the argument (starting at ```1```) followed by ```:```, followed by the argument value and a new line
* Your code should not be executed when imported
* The number of elements of ```argv``` can be retrieved by using: ```len(argv)```
* You do not have to fully understand lists yet, but imagine that ```argv``` can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    if len(argv) - 1 == 1:
        print("{} argument:".format(len(argv) - 1))

    elif len(argv) - 1 == 0:
        print("{} arguments.".format(len(argv) - 1))

    else:
        print("{} arguments:".format(len(argv) - 1))

    for i, args in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, args))
```
</details>

---

## **[3. Infinite addition](3-infinite_add.py)**

Write a program that prints the result of the addition of all arguments

* The output should be the result of the addition of all arguments, followed by a new line
* You can cast arguments into integers by using ```int()``` (you can assume that all arguments can be casted into integers)
* Your code should not be executed when imported
<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":

    total = 0

    for arg in argv[1:]:
        total += int(arg)

    print("{}".format(total))
```
</details>

---

## **[4. Who are you?](4-hidden_discovery.py)**

Write a program that prints all the names defined by the compiled module **hidden_4.pyc** (please download it locally in your sandbox using *curl*).

* This task must be done on the sandbox only
* File 4-hidden_discovery.py must be located on the folder /tmp/
* You should print one name per line, in alpha order
* You should print only names that do **not** start with ```__```
* Your code should not be executed when imported
<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":

    names = dir(hidden_4)

    names_filtered = [name for name in names if not name.startswith("__")]

    names_sorted = sorted(names_filtered)

    for name in names_sorted:
        print("{}".format(name))
```
</details>

---

## **[5. Everything can be imported](5-variable_load.py)**

Write a program that imports the variable ```a``` from the file ```variable_load_5.py``` and prints its value.

* You are not allowed to use ```*``` for importing or ```__import__```
* Your code should not be executed when imported
<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
if __name__ == "__main__":
    from variable_load_5 import a

    print(("{}".format(a)))
```
</details>

---

## **[6. Build my own calculator!](100-my_calculator.py)**

Write a program that imports all functions from the file ```calculator_1.py``` and handles basic operations.

* Usage: ```./100-my_calculator.py a operator b```
    * If the number of arguments is not 3, your program has to:
        * print ```Usage: ./100-my_calculator.py <a> <operator> <b>``` followed with a new line
        * exit with the value ```1```
    * ```operator``` can be:
        * ```+``` for addition
        * ```-``` for subtraction
        * ```*``` for multiplication
        * ```/``` for division
    * If the operator is not one of the above
        * print ```Unknown operator. Available operators: +, -, * and /``` followed with a new line
        * exit with the value ```1```
    * You can cast ```a``` and ```b``` into integers by using ```int()``` (you can assume that all arguments will be castable into integers)
    * The result should be printed like this: ```<a> <operator> <b> = <result>```, followed by a new line
* You are not allowed to use ```*``` for importing or ```__import__```
* Your code should not be executed when imported
<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    if op not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if op == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))

    elif op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))

    elif op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))

    elif op == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
```
</details>

---

## **[7. Easy print](101-easy_print.py)**

**Write a program that prints ```#pythoniscool```, followed by a new line, in the standard output.**

* **Your program should be maximum 2 lines long**

* **You are not allowed to use ```print``` or ```eval``` or ```open``` or ```import sys``` in your file ```101-easy_print.py```**

<details>
<summary>Show answer</summary>

```bash
#!/usr/bin/python3
__import__('sys').stdout.write("#pythoniscool\n")
```
</details>

---

  ### By Anthony Goutieras
  Weekly project from 12/01/26 to 16/01/26 for Holberton School Bordeaux
