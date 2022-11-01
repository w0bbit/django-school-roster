import csv
import os

class Person:

    def __init__(self, name, age, password, role):
        self.name = name
        self.age = age
        self.password = password
        self.role = role

    @classmethod
    def load_all(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(my_path, cls.DATA_FILE)
        
        people = []
        
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                person = cls(**row)
                people.append(person)

        return people
