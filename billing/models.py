from django.db import models
from users_app.models import Enrollments
# Create your models here.

class Payments(models.Model):
    STATUS_CHUSES=[
        ['Cash','Cash'],
        ['Card','Card']
    ]

    enrollment_id = models.ForeignKey(Enrollments, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField