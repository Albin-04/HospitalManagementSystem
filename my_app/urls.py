
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Patient URLs
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:patient_id>/edit/', views.edit_patient, name='edit_patient'),
    path('patients/<int:patient_id>/delete/', views.delete_patient, name='delete_patient'),

    # Doctor URLs
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/add/', views.add_doctor, name='add_doctor'),
    path('doctors/edit/<int:pk>/', views.doctor_update, name='doctor_update'),
    path('doctors/delete/<int:pk>/', views.doctor_delete, name='doctor_delete'),

    # Specializations
    path('specializations/', views.specialization_list, name='specialization_list'),
]
