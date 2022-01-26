from django.shortcuts import render

from doctors.models import DoctorProfile

def DoctorProfilePageView(request,pk):
    doc_id = DoctorProfile.objects.get(pk=pk)
    doc_profiles = DoctorProfile.objects.all()
    return render(request, 'doctor_profile.html',{'doc_id':doc_id,'doc_profiles':doc_profiles})