import django
from django.urls import path
from django import views
from .views import ObjectView,SingleObjectView

urlpatterns = [
    path('', ObjectView, name="home" ),
    path('<int:pk>/', SingleObjectView, name="detail")
]