from django import forms
from hr_app.models import EmployeeDetails,Attachments

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=EmployeeDetails
        fields='__all__'


class DocumentsForm(forms.ModelForm):
    class Meta:
        model=Attachments
        fields='__all__'


