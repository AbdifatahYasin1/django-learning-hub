from django import forms
from .models import Employee, Department, Attendance


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'date_hired': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'

    def clean(self):
        cleaned = super().clean()
        employee = cleaned.get('employee')
        date = cleaned.get('date')

        if employee and date:
            qs = Attendance.objects.filter(
                employee=employee,
                date=date
            )

            if self.instance.pk:
                qs = qs.exclude(pk=self.instance.pk)

            if qs.exists():
                raise forms.ValidationError(
                    "This employee already has attendance for this date."
                )

        return cleaned