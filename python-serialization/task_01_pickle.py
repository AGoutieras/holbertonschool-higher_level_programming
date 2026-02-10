#!/usr/bin/python3

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = str(name)
        self.age = int(age)
        self.is_student = bool(is_student)

    def display(self):
        print(self.name)
        print(self.age)
        print(self.is_student)

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
