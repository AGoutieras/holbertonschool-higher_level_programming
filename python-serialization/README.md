<a href="#"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" /></a>
[![Holberton](https://img.shields.io/badge/Holberton-E31C3F.svg?style=for-the-badge)](https://www.holbertonschool.fr/)

# Python - Serialization

* ## **[0. Basic Serialization](task_00_basic_serialization.py)**

Create a basic serialization module that adds the functionality to serialize a Python dictionary to a JSON file and deserialize the JSON file to recreate the Python Dictionary.

# Instructions:
Write a Python module named ```task_00_basic_serialization.py``` with the following functions:
```python
def serialize_and_save_to_file(data, filename):
    # Your code here to serialize and save data to the specified file
    pass

def load_and_deserialize(filename):
    # Your code here to load and deserialize data from the specified file
    pass
```
The function ```serialize_and_save_to_file``` take 2 parameters:
* ```data```: A Python Dictionary with data
* ```filename```: The filename of the output JSON file. If the output file already exists it should be replaced.

The function ```load_and_deserialize``` take 1 ```parameters```:
* ```filename```: The filename of the input JSON file This function returns a Python Dictionary with the deseialized JSON data from the file.

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3

import json


def serialize_and_save_to_file(data, filename):

    with open(filename, "w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):

    with open(filename, "r") as f:
        return json.load(f)
```
</details>

---

* ## **[1. Pickling Custom Classes](task_01_pickle.py)**

Learn how to serialize and deserialize custom Python objects using the ```pickle``` module.

# Instructions:
1 - Create a custom Python class named ```CustomObject```. This class should have the following attributes:

* ```name``` (a string)
* ```age``` (an integer)
* ```is_student``` (a boolean)

Additionally, the class should have a method display method to print out the object's attributes with the following format:
```
Name: John
Age: 25
Is Student: True
```

2 - Implement two methods within this class:

* ```serialize(self, filename)```: This method will take a filename as its parameter. Using the pickle module, it will serialize the current instance of the object and save it to the provided filename.
* ```@classmethod``` ```deserialize(cls, filename)```: This class method will take a filename as its parameter. Using the pickle module, it will load and return an instance of the ```CustomObject``` from the provided filename.

3 - Save your code in a file named ```task_01_pickle.py```.

> ### Make sure to handle possible exceptions for non-existent or malformed files. If this happens, the methods should return ```None```

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = str(name)
        self.age = int(age)
        self.is_student = bool(is_student)

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
```
</details>

---

* ## **[2. Converting CSV Data to JSON Format](task_02_csv.py)**

The objective of this exercise is to gain experience in reading data from one format (CSV) and converting it into another format (JSON) using serialization techniques.

# Instructions:
1. Begin by importing the required modules:
```python
import csv
import json
```
2. Define a function named ```convert_csv_to_json``` that takes the CSV filename as its parameter and writes the JSON data to ```data.json```.

4. Inside this function:
* Use Python's ```csv``` module to open the CSV file and read the data. Use the ```DictReader``` class to convert each row into a dictionary.
* Serialize the list of dictionaries using the ```json``` module.
* Write the serialized JSON data to ```data.json```.

2. The function should return ```True``` if the conversion was successful.

4. Handle exceptions, such as ```file not found```. Function should return ```False``` in this case.
  
6. Save your work in ```task_02_csv.py```.


<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(filename):

    data_list = []

    with open(filename, "r") as f:
        for row in csv.DictReader(f):
            data_list.append(row)

    try:
        with open("data.json", "w") as f:
            json.dump(data_list, f)
        return True

    except Exception:
        return False
```
</details>

---

* ## **[3. Serializing and Deserializing with XML](task_03_xml.py)**

In this exercise we'll explore serialization and deserialization using XML as an alternative format to JSON.

# Instructions:
Begin by importing the required modules. You can use the ```xml.etree.ElementTree``` module which is a part of Python's standard library for XML processing:
```python
import xml.etree.ElementTree as ET
```

2. Define two main functions:
* ```serialize_to_xml(dictionary, filename)```: This will take a Python dictionary and a filename as parameters. It should serialize the dictionary into XML and save it to the given filename.
* ```deserialize_from_xml(filename)```: This will take a filename as its parameter, read the XML data from that file, and return a deserialized Python dictionary.

2. For ```serialize_to_xml```:
* Create a root element, e.g., ```<data>```.
* Iterate through the dictionary items and add them as child elements to the root.
* Write the XML tree to the provided filename using the ```ET.ElementTree``` class.

2. For ```deserialize_from_xml```:
* Parse the XML file using ```ET.parse```.
* Navigate through the XML elements to reconstruct the dictionary.
* Return the constructed dictionary.

2. Be cautious about data types. XML doesn't differentiate between numbers and strings, etc., like Python does. You might need to manage type conversions.

3. Save your work in ```task_03_xml.py```.

<details>
<summary>Show answer</summary>

```python
#!/usr/bin/python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        dictionary = {}
        for child in root:
            dictionary[child.tag] = child.text
        if 'age' in dictionary:
            dictionary['age'] = int(dictionary['age'])
        if 'is_student' in dictionary:
            dictionary['is_student'] = dictionary['is_student'] == "True"
        return dictionary
    except (FileNotFoundError, ET.ParseError):
        return None
```
</details>

---

  ### By Anthony Goutieras
  Weekly project from 09/02/26 to 13/02/26 for Holberton School Bordeaux
