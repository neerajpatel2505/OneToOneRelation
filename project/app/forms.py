from django import forms
from .models import StudentModel,AadharModel


class Student_Form(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'

class Aadhar_Form(forms.ModelForm):
    class Meta:
        model = AadharModel
        fields = '__all__'
