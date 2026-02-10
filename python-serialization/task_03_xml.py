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
