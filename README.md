# Django School Roster

## Introduction

We're revisiting our School Interface project from before, but now our goal will be to take in data from json files and present them on webpages using Django. Normally, we'd be using databases with Django, however we're not ready for that just yet!

We've provided you with some starter code from our old School Interface project, which already has our classes and data reading logic implemented. You will have to create a Django project from scratch, move some code around, add in some views, templating, and routing logic to eventually produce a website to present our data. We will not be writing (creating/updating/deleting) any new data for this project.

## 1. Create Django Project

Our first step will be to create a Django project. This is something that requires a number of steps, so let's make sure we walk through these steps together here:

0. Navigate into your project directory (if not already in there) in VS Code's terminal

1. Create a virtual environment

```bash
$> python -m venv .venv
```

- This will create a new virtual environment in a folder called `.venv`.
- IMPORTANT: Remember to create a .gitignore file to ignore this entire folder!!! It should not be commited to your git project.

2. Load virtual environment

```bash
$> source .venv/bin/activate
```

- This is the command (for MacOS) to get into the virtual environment. You should see the virtual environment name (".venv") added to your command prompt message.

3. Install Django

```bash
$> pip install django
```

- This command will install the latest Django version into your virtual environment.

4. Save dependency version (optional)

```bash
$> pip freeze > requirements.txt
```

- This command will create a new file and store the results of pip freeze into it.

5. Create Django project

```bash
$> django-admin startproject school_roster_proj .
```

- This command will initialize a new Django project folder with files, and the all important `manage.py`. The "." at the end of the command prevents having nested folders.

6. Create Django app

```bash
$> python manage.py startapp school_roster_app
```

- This command will initialize a new Django application folder with files.

7. Update Django project settings with app name

```python
# school_roster_proj/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "school_roster_app", # added the name of our app
]
```

- This will tell our Django project to also use our newly create app

8. Apply migrations (optional)

```bash
$> python manage.py migrate
```

- This is optional right now, but will remove the warning about "unapplied migrations" when we run our server. You don't need to worry about what this is really doing right now (we'll cover it later on).

9. Launch Server

```bash
$> python manage.py runserver
```

- You should see a message in your terminal stating something like "Starting development server at http://127.0.0.1:8000/"

10. Open a browser and navigate to `http://localhost:8000/`

- If everything worked correctly, you should see a Django rocket lifting off! (This is the default Django landing page.)


## 2. Relocate Logic

Now that we have our initial Django project running, let's move some logic from our provided School Interface files to their appropriate Django locations

### Classes --> app/models.py

Move each of the defined classes from each class file (in the `classes` folder) into `school_roster_app/models.py`. Keep in mind that the order of the classes listed in this file will matter, based on inheritance/composition use. We are moving these classes into `models.py` to just simulate our Django application data models, but keep in mind this is not the official way to create data models in Django. This is a topic we'll have to cover later once we learn about Django Models.

You can delete the original 'classes' folder after this.

### Data

The `data` folder, which contains our json files should remain where they are (to have this work more seemlessly with the provided code). Keep in mind that we normally would be using databases to store our data when using Django, but for now we're stuck with using json data files. 


## 3. Create Views

This is where you're going to have to start to implement some of your own logic for practice! We've created one view handler for you below. You'll need to create the rest of the view logic in `school_roster_app/views.py`! We can't do all the work for you :) 

You should ultimately create views for:

- Home page: Show a link to view all staff, and all students
- List Staff page: Show all staff and link to the staff detail page for each staff member listed. Hint: Use the staff member's employee_id for routing!
- Staff Detail: Show all of the staff data fields on this page (name, age, etc...) for the specified staff member
- List Students page: Show all students and link to the students detail page for each students member listed. Hint: Use the student's school_id for routing!
- Student Detail: Show all of the student data fields on this page (name, age, etc...) for the specified student

```python
# school_roster_app/views.py

from django.shortcuts import render
from .models import School # import our School class

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "pages/index.html", my_data)


def list_staff(request):
    pass # implement


def staff_detail(request, employee_id):
    pass # implement


def list_students(request):
    pass # implement


def student_detail(request, student_id):
    pass # implement
```

## 4. Create Templates

First, you need to create a new directory under your app folder, named "templates". It **MUST** be named exactly that, because this is where Django will automatically look for our templates. We can optionally create another nested directory under "templates", called "pages" (strictly for organizational purposes). We've given you the code for one template file, but you'll have to create others. 

```html
<!-- school_roster_app/templates/pages/index.html -->
<html>
  <head>
    <title>School Page</title>
  </head>
  <body>
    <h2>{{school_name}} Directory</h2>
    <ul>
      <li><a href={% url 'list_staff' %}>All Staff</a></li>
      <li><a href={% url 'list_students' %}>All Student</a></li>
    </ul>
  </body>
</html>
```

## 5. Create Routing

1. Update project's urls.py

```python
# school_roster_proj/urls.py

from django.contrib import admin
from django.urls import path, include # add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path("school/", include("school_roster_app.urls")), # add this
]
```

2. Create a new `urls.py` file for your app

```python
# school_roster_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("staff/", views.list_staff, name="list_staff"),
    path("staff/<int:employee_id>/", views.staff_detail, name="staff_detail"),
    path("students/", views.list_students, name="list_students"),
    path("students/<int:student_id>/", views.student_detail, name="student_detail"),
]
```

## 6. Release Application

Once you've completed all of the required steps above, make sure you test your finished product. Run your server, go to your home page ("http://localhost:8000/school/"), and make sure all of your links work. To review, you should have 5 routes and pages, and proper linking between each!

- Home page
- All Staff page
- Staff Detail page
- All Students page
- Student Detail page

## 7. Bonus: CSS Styling

Add some CSS styling to your HTML templates. Here's the Django resource that might help you achieve this: https://docs.djangoproject.com/en/4.0/howto/static-files/
