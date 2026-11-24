from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department
from .forms import EmployeeForm, DepartmentForm


def employee_list(request):
    employees = Employee.objects.select_related('department').all()
    return render(request, 'employee_list.html', {'employees': employees})


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
    departments = Department.objects.all()
    return render(request, 'department_list.html', {'departments': departments})


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