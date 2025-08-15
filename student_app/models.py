from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class StudentProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_data = models.DateField(null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)
    parent_name = models.CharField(max_length=50,blank=True)
    parent_phone = models.CharField(max_length=15, blank=True)


    def __str__(self):
        return self.user.first_name