from django.contrib import admin
from .models import Patient,Doctors,Specialization

admin.site.register(Patient)
admin.site.register(Doctors)
admin.site.register(Specialization)