from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.load_all()
        self.students = Student.load_all()

    def find_student_by_id(self, school_id):
        for student in self.students:
            if student.school_id == school_id:
                return student
        
        return None

    def find_staff_by_id(self, employee_id):
        for staff in self.staff:
            if staff.employee_id == employee_id:
                return staff
        
        return None