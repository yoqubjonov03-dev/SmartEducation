from django.db import models
from users_app.models import Enrollments
# Create your models here.

class Payments(models.Model):
    CASH = 'Cash'
    CARD = 'Card'
    STATUS_CHOICES=[
        [CASH,'Cash'],
        [CARD,'Card']
    ]

    enrollment_id = models.ForeignKey(Enrollments, on_delete=models.CASCADE)
    stripe_charge_id = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=STATUS_CHOICES, default= CASH)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.enrollment_id.student_id.user.get_full_name()



