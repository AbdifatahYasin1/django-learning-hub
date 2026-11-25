from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department,Attendance
from .forms import EmployeeForm, DepartmentForm, AttendanceForm
from django.db.models import Q


def employee_list(request):
    q = request.GET.get('q' , '')
    employees = Employee.objects.all()
    if q: 
        employees =employees.filter(
             Q(first_name__icontains=q) | 
             Q(last_name__icontains=q) | 
             Q(email__icontains=q) |
             Q(position__icontains=q) 
        )
    return render(request, 'employee_list.html', {'employees': employees, 'q' : q})



def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form, 'title': 'Add Employee'})


def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form, 'title': 'Edit Employee'})


def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})


def department_list(request):
    q = request.GET.get('q' , '')
    departments = Department.objects.all()
    if q: 
        departments = departments.filter( Q(name__icontains=q) | Q(description__icontains=q))
    return render(request, 'department_list.html', {'departments': departments,'q' : q})


def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm()
    return render(request, 'employee_form.html', {'form': form, 'title': 'Add Department'})


def department_update(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'employee_form.html', {'form': form, 'title': 'Edit Department'})


def department_delete(request, pk):
    department = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        department.delete()
        return redirect('department_list')
    return render(request, 'department_confirm_delete.html', {'department': department})

def attendance_list(request):
       q = request.GET.get('q' , '')
       records = Attendance.objects.select_related('employee').order_by('-date')
       if q: 
         records = records.filter( 
             Q(employee__first_name__icontains=q) |
             Q(employee__last_name__icontains=q) |
               Q(status__icontains=q))
       return render(request, 'attendance_list.html', {'records': records,'q': q})


def attendance_create(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm()
    return render(request, 'employee_form.html', {'form': form, 'title': 'Add Attendance'})


def attendance_update(request, pk):
    record = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else:
        form = AttendanceForm(instance=record)
    return render(request, 'employee_form.html', {'form': form, 'title': 'Edit Attendance'})


def attendance_delete(request, pk):
    record = get_object_or_404(Attendance, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('attendance_list')
    return render(request, 'attendance_confirm_delete.html', {'record': record})