import django
from django.urls import path
from django import views
from .views import DoctorProfilePageView


urlpatterns = [
    path('<int:pk>/', DoctorProfilePageView,name="doctor_profile" )
]