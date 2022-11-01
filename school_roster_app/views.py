from django.shortcuts import render
from .models import School, Person, Staff, Student

# Create your views here.
my_school = School("Django School")

def index(request):
  data = {"school_name":my_school.name}
  return render(request, 'pages/index.html', data)

def list_staff(request):
  data = {'list_staff':my_school.staff}
  return render(request, 'pages/list_staff.html', data)

def staff_detail(request, employee_id):
  data = {'staff':my_school.find_staff_by_id(employee_id)}
  return render(request, 'pages/staff_detail.html', data)

def list_students(request):
  data = {'list_students':my_school.students}
  return render(request, 'pages/list_students.html', data)

def student_detail(request, student_id):
  data = {'student':my_school.find_student_by_id(student_id)}
  return render(request, 'pages/student_detail.html', data)
