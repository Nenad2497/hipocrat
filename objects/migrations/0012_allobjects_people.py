# Generated by Django 4.0.1 on 2022-01-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_remove_doctorprofile_work_place'),
        ('objects', '0011_remove_allobjects_doctors'),
    ]

    operations = [
        migrations.AddField(
            model_name='allobjects',
            name='people',
            field=models.ManyToManyField(to='doctors.DoctorProfile'),
        ),
    ]