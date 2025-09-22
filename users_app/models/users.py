from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class StudentProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    parent_name = models.CharField(max_length=50,blank=True)
    parent_phone = models.CharField(max_length=15, blank=True)


    def __str__(self):
        return self.user.username

class TeacherProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=50)
    experience_years = models.PositiveIntegerField(default=0)
    address = models.TextField(max_length=255,null=True, blank=True)

    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username