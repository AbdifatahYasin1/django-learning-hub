# Group 3 - Employee Management System

A web application built with **Django** for managing employees, departments and attendance.

## Features

- **Employees:** add, view, edit, delete (CRUD)
- **Departments:** add, view, edit, delete (CRUD)
- **Attendance:** record daily attendance (Present, Absent, Late, On Leave), edit and delete
- **Search:** search employees, departments and attendance records
- **Form validation:** required fields, valid email, unique email, one attendance record per employee per day
- **Navigation bar** and responsive design with Bootstrap

## Technologies

Python, Django, HTML, CSS, Bootstrap 5, SQLite

## Database Design

- **Department** (name, description)
- **Employee** (first name, last name, email, phone, position, salary, date hired, department)
- **Attendance** (employee, date, status, note)

Relationships: one Department has many Employees; one Employee has many Attendance records.

## How to Run

1. Clone the repository and open the project folder:

```
git clone https://github.com/Nashad2025/django-learning-hub.git
cd django-learning-hub/group3_employee_system
```

2. Create and activate a virtual environment (Windows):

```
python -m venv env
env\Scripts\activate
```

3. Install Django:

```
pip install -r requirements.txt
```

4. Create the database (the database file is not included in the repository):

```
python manage.py migrate
```

5. Create an admin user (optional, for the admin panel):

```
python manage.py createsuperuser
```

6. Start the server:

```
python manage.py runserver
```

7. Open http://127.0.0.1:8000/ in your browser. The admin panel is at http://127.0.0.1:8000/admin/

## Group Members and Responsibilities

| Member | Responsibility |
|--------|----------------|
| Nashad Farxaan Axmed | Project setup, models, CRUD (employees, departments, attendance), templates, search, README |
| Mubarig Cabdi Cabdillahi 
| Asiya Axmed Siciid | departments improvements,validation ,documentation|
| Samira Kayse Suluub 
| Abokor Clrashiid Axmed 
| Khalid Mahamed Farah 
