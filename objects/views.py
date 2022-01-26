from dataclasses import field
from django.shortcuts import render

from django.views.generic import DetailView,ListView

from doctors.models import DoctorProfile

from . models import AllObjects


def ObjectView(request):
    models = AllObjects.objects.all()
    return render(request, 'index.html',{'models':models})


def SingleObjectView(request,pk):
    object = AllObjects.objects.get(pk=pk)
    doctors = DoctorProfile.objects.all()
    return render(request, 'object.html',{'object':object,'doctors':doctors})
