from django.db import models
from django.contrib.auth.models import User


class DoctorProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to="images")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    specialization =models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)