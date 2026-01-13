# Python - if/else, loops, functions

[0. Positive anything is better than negative nothing](0-positive_or_negative.py): This program will assign a random signed ```number``` to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable ```number``` is positive or negative.

* You can find the source code [here](https://github.com/hs-hq/0x01.py/blob/main/0-positive_or_negative.py)
* The variable ```number``` will store a different value every time you will run this program
* You don’t have to understand what ```import```, ```random.randint``` do. Please do not touch this code
* The output of the program should be:
  * The number, followed by
    * if the number is greater than 0: ```is positive```
    * if the number is 0: ```is zero```
    * if the number is less than 0: ```is negative```
  * followed by a new line
    <details>
    <summary>Show answer</summary>

    ```bash
    #!/usr/bin/python3
    import random
    number = random.randint(-10, 10)
    
    if number > 0:
        print("{} is positive".format(number))
    
    if number == 0:
        print("{} is zero".format(number))
    
    if number < 0:
        print("{} is negative".format(number))
    ```
---
[1. The last digit](1-last_digit.py): This program will assign a random signed ```number``` to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable ```number```.

* You can find the source code [here](https://github.com/hs-hq/0x01.py/blob/main/1-last_digit_py)
* The variable ```number``` will store a different value every time you will run this program
* You don’t have to understand what ```import```, ```random.randint``` do. Please do not touch this code. This line should not change: ```number = random.randint(-10000, 10000)```
* The output of the program should be:
  * The string ```Last digit of```, followed by
  * the number, followed by
  * the string ```is```, followed by the last digit of ```number```, followed by
    * if the last digit is greater than 5: the string ```and is greater than 5```
    * if the last digit is 0: the string ```and is 0```
    * if the last digit is less than 6 and not 0: the string ```and is less than 6 and not 0```
  * followed by a new line
    <details>
    <summary>Show answer</summary>

    ```bash
    #!/usr/bin/python3
    import random
    number = random.randint(-10000, 10000)
    
    
    last = abs(number) % 10
    
    if last > 5:
        msg = "and is greater than 5"
    
    elif last == 0:
        msg = "and is zero"
    
    else:
        msg = "and is less than 6 and not 0"
    
    print("last digit of {} is {} {}".format(number, last, msg))
    ```
---
[2. I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game](2-print_alphabet.py): Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

* Use only one ```print``` function with string format
* Use only one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module
    <details>
    <summary>Show answer</summary>

    ```bash
    #!/usr/bin/python3
    for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
    ```
---
[3. When I was having that alphabet soup, I never thought that it would pay off](3-print_alphabt.py): Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

* Print all the letters except ```q``` and ```e```
* You can only use one ```print``` function with string format
* You can only use one loop in your code
* You are not allowed to store characters in a variable
* You are not allowed to import any module
    <details>
    <summary>Show answer</summary>

    ```bash
    #!/usr/bin/python3
    for letter in range(97, 123):
    if letter != 101 and letter != 113:
        print("{}".format(chr(letter)), end="")
    ```
---
[4. Hexadecimal printing](4-print_hexa.py): Write a program that prints all numbers from ```0``` to ```98``` in decimal and in hexadecimal (as in the following example)

* You can only use one ```print``` function with string format
* You can only use one loop in your code
* You are not allowed to store numbers or strings in a variable
* You are not allowed to import any module
    <details>
    <summary>Show answer</summary>

    ```bash
    #!/usr/bin/python3
    for num in range(0, 99):
    print("{} = {}".format(num, hex(num)))
    ```
---
[5. 00...99](5-print_comb2.py): 

* 
    <details>
    <summary>Show answer</summary>

    ```bash

    ```
---
[6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
](6-print_comb3.py): 

* 
    <details>
    <summary>Show answer</summary>

    ```bash

    ```
---
[7. islower](7-islower.py): 

* 
    <details>
    <summary>Show answer</summary>

    ```bash

    ```
---
[8. To uppercase](8-uppercase.py): 

* 
    <details>
    <summary>Show answer</summary>

    ```bash

    ```
---
[9. There are only 3 colors, 10 digits, and 7 notes; it's what we do with them that's important](9-print_last_digit.py): 

* 
    <details>
    <summary>Show answer</summary>

    ```bash

    ```
---
[10. a + b](10-add.py): 

* 
    <details>
    <summary>Show answer</summary>

    ```bash

    ```
---
[11. a ^ b](11-pow.py): 

* 
    <details>
    <summary>Show answer</summary>

    ```bash

    ```
---
[12. Fizz Buzz](12-fizzbuzz.py): 

* 
    <details>
    <summary>Show answer</summary>

    ```bash

    ```
---
[](): 

* 
    <details>
    <summary>Show answer</summary>

    ```bash

    ```
---
[](): 

* 
    <details>
    <summary>Show answer</summary>

    ```bash

    ```
---
