# Generated by Django 4.0.1 on 2022-01-26 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_remove_doctorprofile_work_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorprofile',
            name='slug',
            field=models.SlugField(default=11),
            preserve_default=False,
        ),
    ]
