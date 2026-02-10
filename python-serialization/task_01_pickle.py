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
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
            return obj
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
