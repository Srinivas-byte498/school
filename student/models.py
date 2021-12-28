from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=120, null=True)
    last_name = models.CharField(max_length=120, null=True)
    email = models.CharField(max_length=256, null=True)
    ph_num = models.CharField(max_length=20, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=30, null=True)
    first_lang = models.CharField(max_length=60, null=True)
