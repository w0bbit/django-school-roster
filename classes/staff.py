import csv
import os.path
from classes.person import Person

class Staff(Person):
    DATA_FILE = "../data/staff.csv"

    def __init__(self, name, age, password, role, employee_id):
        super().__init__(name, age, password, role)
        self.employee_id = employee_id

    def __repr__(self):
        return f"staff: {self.name}"