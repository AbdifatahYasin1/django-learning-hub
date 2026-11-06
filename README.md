# Django Learning Hub

A beginner-friendly Django course repository to help students learn core concepts like models, views, templates, forms, and authentication through hands-on examples and a group project.

---

## 📑 Table of Contents

- [🛠️ Installation Guide](#️-installation-guide)
- [📚 Learning Topics](#-learning-topics)
- [🧪 Exercises](#-exercises)
- [🚀 Group Project Assignment](#-django-web-development--group-project-assignment)
- [📂 Resources](#-resources)
- [📊 Slides & Presentation](#-slides--presentation)
- [💡 Final Exam Hints](#-final-exam-hints)
- [🙌 Contributors](#-contributors)

---

## 🛠️ Installation Guide

### Prerequisites

- Python 3.10+
- pip
- Git
- A code editor like VS Code or PyCharm

### Step-by-Step Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/AbdifatahYasin1/django-learning-hub.git
   cd django-learning-hub
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. **Install Django**

   ```bash
   pip install django
   ```

4. **Create a Django project and app**

   ```bash
   django-admin startproject mysite .
   python manage.py startapp myapp
   ```

5. **Apply migrations and start the development server**

   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

   Open <http://127.0.0.1:8000/> in your browser.

---

## 📚 Learning Topics

### ✅ Core Django Concepts

* Django project structure
* Apps, models, and migrations
* Views and URL routing
* HTML templating with Django
* Forms and ModelForms
* Authentication (login/logout/register)
* Admin panel customization

### ✅ Optional Topics

* Class-based views (CBVs)
* Static and media files
* Sending emails
* Pagination
* REST APIs with Django REST Framework (DRF)

---

## 🧪 Exercises

### 1. Django Basics

* Create a new Django project and app
* Setup project-level and app-level URLs
* Render a homepage using a basic view and template

### 2. Models & Database

* Create a `Student` model with fields: name, age, email, course
* Use the Django admin to add data
* Display model data on a page

### 3. Forms & Templates

* Build a contact form using `forms.Form`
* Use `ModelForm` to create/update a student object
* Show validation errors in template

### 4. Authentication

* Build user registration and login/logout views
* Restrict access to views for authenticated users
* Display user info on navbar

### 5. Mini Project Ideas

* Blog app (posts, comments, tags)
* Task manager (CRUD operations)
* Notes app with user login

---

# 🚀 Django Web Development – Group Project Assignment

| Item | Details |
|------|---------|
| **Classes** | Morning Students (5 groups) · Afternoon Students (9 groups) · Evening Students (3 groups) |
| **Repository** | [django-learning-hub](https://github.com/AbdifatahYasin1/django-learning-hub.git) |
| **Duration** | Three weeks from the date of announcement |
| **Final Deadline** | 🗓️ 27 November 2026 |
| **Total Marks** | 20 |
| **Technology** | Python, Django, HTML, CSS, Bootstrap, SQLite |

---

## ⚙️ 1. General Project Requirements

Every group must develop one complete web application using the Django framework. Each project must:

1. Use **Django** as the backend framework.
2. Create appropriate Django **models** and database relationships where necessary.
3. Implement **CRUD** operations:
   - Create records.
   - Read and display records.
   - Update existing records.
   - Delete records.
4. Implement Django **views** and **URL routing**.
5. Use Django **templates** to build the user interface.
6. Use **HTML, CSS, and Bootstrap** for frontend design.
7. Use **SQLite** as the database.
8. Include **form validation**.
9. Implement **search** functionality where appropriate.
10. Provide a working **navigation** system.
11. Include a **README.md** file explaining the project and how to run it.

---

## 🤝 2. GitHub Collaboration Requirements

GitHub collaboration is **COMPULSORY** for every student. Every group must:

- Fork or collaborate using the instructor's repository, following the instructor's GitHub instructions.
- Create a dedicated project folder or repository for its assigned project.
- Work collaboratively using Git and GitHub.
- Make at least **THREE meaningful commits per student**.
- Push their contributions to GitHub.
- Use meaningful commit messages.
- Share responsibilities among group members.
- Review and integrate other members' contributions.

> ⚠️ **Important:** Each student must personally contribute at least three commits. Copying another student's commits or making meaningless commits will not count. The instructor will check the GitHub commit history to verify individual contributions.

---

## 📌 3. Timeline and Deadline

| Week | Focus |
|------|-------|
| **Week 1** | Project planning, requirements analysis, database design, and initial Django setup |
| **Week 2** | Backend development, models, views, CRUD functionality, and frontend implementation |
| **Week 3** | Testing, debugging, GitHub collaboration, documentation, and final submission |

**Final Deadline: 🗓️ 27 November 2026**

### 📤 Submission

Each group must submit:

1. GitHub repository link.
2. Complete working Django application.
3. README.md documentation.
4. List of group members and their responsibilities.
5. Final project demonstration.

---

## 📝 4. Assessment Criteria (Total: 20 Marks)

| Assessment Criteria | Marks |
|---------------------|------:|
| Django functionality and CRUD operations | 5 |
| Database design and models | 3 |
| Frontend design and user experience | 2 |
| GitHub collaboration and individual commits | 4 |
| Project organization and code quality | 2 |
| Final presentation and demonstration | 2 |
| README and documentation | 2 |
| **Total** | **20 Marks** |

GitHub collaboration will be evaluated individually as well as at group level.

---

## 🌅 5. Morning Students – Group Assignments

| Group | Project |
|-------|---------|
| Group 1 | Student Management System |
| Group 2 | Library Management System |
| Group 3 | Hospital Management System |
| Group 4 | Inventory Management System |
| Group 5 | Online Course Management System |

### Group 1 – Student Management System

**Members:**
1. Mubarik Xasan
2. Faadumo
3. Axmed Maxamed
4. Ridwaan
5. Asma
6. Cabdirasaaq

**Project requirements:**
- Register new students.
- Manage student information.
- Update and delete student records.
- Organize students by department or class.
- Search students by name or student ID.
- Display student lists and details.

### Group 2 – Library Management System

**Members:**
1. Maxamed Abiib
2. Nimco
3. Subeer
4. Muxiyadiin
5. Najma
6. Khadar

**Project requirements:**
- Register books.
- Manage book categories.
- Register library members.
- Borrow and return books.
- Track available and borrowed books.
- Search books by title or author.

### Group 3 – Hospital Management System

**Members:**
1. Mubarik Cabdi
2. Raxma
3. Ahmed Sheekh
4. Shafici
5. Shucayb

**Project requirements:**
- Register patients.
- Manage doctors.
- Schedule appointments.
- Store patient visit records.
- Manage departments.
- Search patient records.

### Group 4 – Inventory Management System

**Members:**
1. Abdikarim
2. Sakariye Maxamed
3. Najax
4. Abdiqadir
5. Mubarik Mustafe

**Project requirements:**
- Register products.
- Manage product categories.
- Track stock quantities.
- Record purchases and sales.
- Update inventory.
- Display low-stock products.

### Group 5 – Online Course Management System

**Members:**
1. Abdirahman
2. Cabdixakim
3. Sakariye Ali
4. Khaliil
5. Badri

**Project requirements:**
- Register students.
- Create and manage courses.
- Enroll students in courses.
- Assign instructors.
- Display available courses.
- Track student enrollment.

---

## 🌇 6. Afternoon Students – Group Assignments

| Group | Project |
|-------|---------|
| Group 1 | Online Shopping System |
| Group 2 | Hotel Management System |
| Group 3 | Employee Management System |
| Group 4 | School Management System |
| Group 5 | Blood Donor Management System |
| Group 6 | Online Job Portal |
| Group 7 | School Attendance Management System |
| Group 8 | Event Management System |
| Group 9 | Restaurant Management System |

### Group 1 – Online Shopping System

**Members:**
1. Axmed Faysal Axmed
2. Sumaya Ibrahim Ali
3. Khadar Salaad Axmed
4. Mumtaas Cabdi Ibraahib
5. Barwaqo Cabdilahi Meecaad
6. Zaki Hasan Dool

**Project requirements:**
- Manage products and categories.
- Display products.
- Add products to a shopping cart.
- Manage customer information.
- Place and manage orders.
- Track order status.

### Group 2 – Hotel Management System

**Members:**
1. Sareedo Axmed Aadan
2. Sakariye Maxamed Cumar
3. Hana C/qani Jamaac
4. Nasri Faysal Cabdi
5. Subayd Naasir Dahir
6. Nuura Ismaaciil Cabdi

**Project requirements:**
- Register hotel rooms.
- Manage room categories.
- Register customers.
- Make room reservations.
- Check room availability.
- Manage check-in and check-out records.

### Group 3 – Employee Management System

**Members:**
1. Nashad Farxaan Axmed
2. Mubarig Cabdi Cabdillahi
3. Asiya Axmed Siciid
4. Samira Kayse Suluub
5. Abokor Clrashiid Axmed
6. Khalid Mahamed Farah

**Project requirements:**
- Register employees.
- Manage departments.
- Store employee information.
- Update employee records.
- Track employee attendance.
- Search employees.

### Group 4 – School Management System

**Members:**
1. Arwa Yuusuf Cali
2. Maxamed Jamac Maxamuud
3. Xafsa Clraxmaan Cumar
4. Amiir Husen Xasan
5. Asma Ismacil Raabi
6. Cismaan Buudul Cismaan

**Project requirements:**
- Register students.
- Manage teachers.
- Create classes.
- Manage subjects.
- Record student marks.
- Display student results.

### Group 5 – Blood Donor Management System

**Members:**
1. Clqani Mahamed Diriye
2. Mulki Mustafe Nuur
3. Safa Xasan Axmed
4. Sharmake Clxakiin Maxamed
5. Yaxye Khadar Maxamed
6. Mayaa Guleed Xasan

**Project requirements:**
- Register blood donors.
- Record blood groups.
- Store donor contact information.
- Search donors by blood group.
- Search donors by city.
- Manage donor availability.

### Group 6 – Online Job Portal

**Members:**
1. Axmed Cabdi Maxamed
2. Isra Axmed Ismaaciil
3. Dahabo Clrashiid Yuusuf
4. Mubarig Jama Kahin
5. Cadnan Axmed Cayngal
6. Raxma Clkariin Roble

**Project requirements:**
- Register job seekers.
- Create and manage job vacancies.
- Allow applicants to apply for jobs.
- Upload or record CV information.
- Manage applications.
- Search jobs by category.

### Group 7 – School Attendance Management System

**Members:**
1. Salma Quresh Cabdi
2. Clraxmaan Maxamed Muuse
3. Sakariye Clsaalan Maxamed
4. Maxamuud Muuse Clraxmaan
5. Hodoo Mawliid Xasan
6. Mustafe Abdisamad Mohamoud

**Project requirements:**
- Register students.
- Manage classes.
- Record daily attendance.
- Mark students present or absent.
- Generate attendance reports.
- Search attendance by date and student.

### Group 8 – Event Management System

**Members:**
1. Omar Clraxmaan Omar
2. Ugbad Ali Mahamed
3. Landna Maxamed Maxamud
4. Samira Maxamed Adani
5. Cabdikhaliq Maxamuud Japane

**Project requirements:**
- Create and manage events.
- Register participants.
- Manage event categories.
- Allow participants to register for events.
- Track event registrations.
- Display upcoming events.

### Group 9 – Restaurant Management System

**Members:**
1. Hodoo Maxamuud Axmed
2. Clfatax Omer Husen
3. Maxamed Axmed Nuur
4. Cawo Muuse Jamaac
5. Xanan Axmed Xasan

**Project requirements:**
- Manage food menu items.
- Organize food categories.
- Register customers.
- Create and manage orders.
- Calculate order totals.
- Track order status.

---

## 🌙 7. Evening Students – Group Assignments

| Group | Project |
|-------|---------|
| Group 1 | Pharmacy Management System |
| Group 2 | Bus Ticket Booking System |
| Group 3 | Property Rental Management System |

### Group 1 – Pharmacy Management System

**Members:**
1. Muktatr Abirahman Wayrax
2. Liban Abdirisaq Hassan
3. Hothan Mohamed Omer
4. Mohamed Hamud Tukale
5. Ismail Abdirahman Muumin
6. Jamal

**Project requirements:**
- Register medicines.
- Manage medicine categories.
- Track stock quantities and expiry dates.
- Register customers.
- Record medicine sales.
- Search medicines by name or category.

### Group 2 – Bus Ticket Booking System

**Members:**
1. Guleth Bader Yousuf
2. Muna Ahmed Abdirahman
3. Khalid Ahmed Osman
4. Ahmed Abdishakur Hassan
5. Mohamed Abdi Ahmed
6. Ahmed Mohamed Omar
7. Abokor

**Project requirements:**
- Register buses.
- Manage routes and schedules.
- Register passengers.
- Book and cancel tickets.
- Check seat availability.
- Search trips by route and date.

### Group 3 – Property Rental Management System

**Members:**
1. Suhayb Mohamed Hamud
2. Adem Mohamed Abdi
3. Mohamed Yousuf Elmi
4. Wacays Said Ali
5. Mustafe Adan Abdi
6. Awo Mahamed Omar

**Project requirements:**
- Register properties.
- Manage property types.
- Register tenants.
- Create and manage rental agreements.
- Record rent payments.
- Search available properties by location.

---

## 🎤 8. Final Submission and Presentation

Every group must demonstrate its application to the instructor. During the presentation, students must demonstrate:

1. How their Django application works.
2. Database models and relationships.
3. CRUD operations.
4. User interface and navigation.
5. GitHub repository and commit history.
6. Each member's contribution.

The instructor may ask any group member to explain or demonstrate any part of the application. **Every student must understand the project, not just their assigned section.**

---

## ❗ 9. Important Rules

- All projects must be developed using **Django**.
- GitHub collaboration is **compulsory**.
- Every student must have at least **three meaningful commits**.
- Copying projects from other groups is **prohibited**.
- Every group member must participate.
- The instructor may individually question any student.
- Late submissions may receive a penalty.
- The final project is worth **20 marks**.

**Good luck to everyone! 🎉**

*Instructor – Django Web Development Course*

---

## 📂 Resources

### 📘 Official Django Documentation

| Topic | Link |
|-------|------|
| Django documentation (home) | [docs.djangoproject.com](https://docs.djangoproject.com/en/stable/) |
| Official beginner tutorial (polls app) | [Writing your first Django app](https://docs.djangoproject.com/en/stable/intro/tutorial01/) |
| Models and field types | [Model field reference](https://docs.djangoproject.com/en/stable/ref/models/fields/) |
| ORM – making queries | [Making queries](https://docs.djangoproject.com/en/stable/topics/db/queries/) |
| Forms and validation | [Working with forms](https://docs.djangoproject.com/en/stable/topics/forms/) |
| Authentication | [User authentication in Django](https://docs.djangoproject.com/en/stable/topics/auth/) |

### 🎓 Tutorials and Books

- [Django Girls Tutorial](https://tutorial.djangogirls.org/en/) – step-by-step for absolute beginners
- [MDN Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) – builds a full library website
- [W3Schools Django Tutorial](https://www.w3schools.com/django/) – short, practical lessons
- [Real Python – Django Tutorials](https://realpython.com/tutorials/django/)
- [Django for Beginners (Book)](https://djangoforbeginners.com/)
- [Simple is Better Than Complex](https://simpleisbetterthancomplex.com/) – articles on common Django tasks
- [Django REST Framework](https://www.django-rest-framework.org/) – optional, for building APIs

### 🎨 Bootstrap

- [Bootstrap 5.3 – Getting Started](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Official Bootstrap Documentation](https://getbootstrap.com/docs/)
- [Bootstrap Icons](https://icons.getbootstrap.com/)
- [Bootstrap 5 Tutorial – W3Schools](https://www.w3schools.com/bootstrap5/)
- [Bootstrap Cheat Sheet](https://bootstrap-cheatsheet.themeselection.com/)
- [Bootstrap Components – MDBootstrap](https://mdbootstrap.com/docs/standard/)
- [Free Bootstrap Templates – Start Bootstrap](https://startbootstrap.com/)

### 🐙 Git and GitHub (required for the group project)

- [GitHub Hello World](https://docs.github.com/en/get-started/start-your-journey/hello-world) – repositories, branches, commits, pull requests
- [Fork a Repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
- [Pro Git Book (free)](https://git-scm.com/book/en/v2)

### 🎥 Video Tutorials

| Video | Channel | Topic |
|-------|---------|-------|
| [Python Django Web Framework – Full Course for Beginners](https://www.youtube.com/watch?v=F5mRW0jo-U4) | freeCodeCamp.org | Django |
| [Python Django Crash Course](https://www.youtube.com/watch?v=e1IyzVyrLSU) | Traversy Media | Django |
| [Django Tutorial: Full-Featured Web App Part 1](https://www.youtube.com/watch?v=UmljXZIypDc) | Corey Schafer | Django |
| [Bootstrap 5 Crash Course – Website Build & Deploy](https://www.youtube.com/watch?v=4sosXZsdy-s) | Traversy Media | Bootstrap |
| [Bootstrap 5 Crash Course](https://www.youtube.com/watch?v=Jyvffr3aCp0) | Web Dev Simplified | Bootstrap |

---

## 📊 Slides & Presentation

You can find the slides and presentation materials here:  
[**Chapter One**](ChapterOne.pptx)

---

## 💡 Final Exam Hints

- Understand how Django handles routing via `urls.py`
- Know how to use models to define data structures
- Be able to use Django ORM for queries
- Understand form submission and validation
- Build and protect views using decorators like `@login_required`
- Reuse HTML using Django template tags safely, as shown below to avoid Jekyll errors:

   ```django
   {% raw %}
   {% extends "base.html" %}
   {% block content %}
   <!-- Your content here -->
   {% endblock %}
   {% endraw %}
   ```

---

## 🙌 Contributors

See [CONTRIBUTORS.md](CONTRIBUTORS.md) for everyone who has contributed to this repository. Students: add your name and GitHub profile link there as one of your commits.
