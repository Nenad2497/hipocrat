from django.db import models
from django.contrib.auth.models import User

from doctors.models import DoctorProfile

class AllObjects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    working_h = models.CharField(max_length=255)
    lat = models.DecimalField(max_digits=20, decimal_places=8)
    lng = models.DecimalField(max_digits=20, decimal_places=8)
    
    
    def __str__(self):
        return str(self.name)