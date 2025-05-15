from django import forms
from .models import Patient
from .models import Doctors



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorsForm(forms.ModelForm):
    class Meta:
        model = Doctors
        fields = ['id','name', 'specialization', 'phone', 'email']

