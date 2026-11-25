from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employees/add/', views.employee_create, name='employee_create'),
    path('employees/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employees/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/add/', views.department_create, name='department_create'),
    path('departments/<int:pk>/edit/', views.department_update, name='department_update'),
    path('departments/<int:pk>/delete/', views.department_delete, name='department_delete'),
    path('attendance/' , views.attendance_list, name='attendance_list'),
     path('attendance/add/', views.attendance_create,name='attendance_create'),
    path('attendance/<int:pk>/edit/', views.attendance_update,name='attendance_update'),
    path('attendance/<int:pk>/delete/', views.attendance_delete,name='attendance_delete'),

]