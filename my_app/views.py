# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, Doctors, Specialization
from .forms import PatientForm, DoctorsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Public Pages
def index(request):
    return render(request, 'my_app/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'my_app/login.html', {'error': 'Invalid credentials'})
    return render(request, 'my_app/login.html')

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        if not username:
            return render(request, 'my_app/signup.html', {'error': 'Username cannot be empty.'})
        if not password:
            return render(request, 'my_app/signup.html', {'error': 'Password cannot be empty.'})
        if User.objects.filter(username=username).exists():
            return render(request, 'my_app/signup.html', {'error': 'Username already exists.'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'my_app/signup.html')

def logout_view(request):
    logout(request)
    return redirect('index')

# Dashboard
@login_required
def dashboard(request):
    return render(request, 'my_app/dashboard.html')

# Patient Views
@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'my_app/patient_list.html', {'patients': patients})

@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'my_app/add_patient.html', {'form': form})

@login_required
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    return render(request, 'my_app/patient_detail.html', {'patient': patient})

@login_required
def edit_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'my_app/edit_patient.html', {'form': form})

@login_required
def delete_patient(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'my_app/delete_patient.html', {'patient': patient})

# Doctor Views
@login_required
def doctor_list(request):
    doctor = Doctors.objects.all()
    return render(request, 'my_app/doctor_list.html', {'doctor': doctor})

@login_required
def add_doctor(request):
    success = False
    if request.method == 'POST':
        form = DoctorsForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = DoctorsForm()
    else:
        form = DoctorsForm()
    return render(request, 'my_app/add_doctor.html', {'form': form, 'success': success})

@login_required
def doctor_update(request, pk):
    doctor = get_object_or_404(Doctors, pk=pk)
    form = DoctorsForm(request.POST or None, instance=doctor)
    if form.is_valid():
        form.save()
        return redirect('doctor_list')
    return render(request, 'my_app/doctor_form.html', {'form': form})

@login_required
def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctors, pk=pk)
    doctor.delete()
    return redirect('doctor_list')

@login_required
def specialization_list(request):
    specializations = Specialization.objects.all()
    return render(request, 'my_app/specialization_list.html', {'specializations': specializations})
