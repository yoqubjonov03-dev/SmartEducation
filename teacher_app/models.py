from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TeacherProfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=50)
    exprence_years = models.PositiveIntegerField(default=0)
    address = models.TextField(max_length=255,null=True, blank=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.first_name