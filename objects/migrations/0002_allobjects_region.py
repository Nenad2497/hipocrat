# Generated by Django 4.0.1 on 2022-01-25 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='allobjects',
            name='region',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
