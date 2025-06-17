from django import forms
from record.models import Employee
class addemployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['Name','Age','Salary','Designation','Place','Image','Department_Name']