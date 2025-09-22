from django.db import models
from django.db.models import CharField

from .users import TeacherProfil, StudentProfil


class Courses(models.Model):
    """Curslar saqlash uchun"""
    MONTHS = 'months'
    WEEKS = 'weeks'

    STATUS_CHOICES = [
        (MONTHS, 'Months'),
        (WEEKS, 'Weeks'),
    ]

    name = models.CharField(max_length=55)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=50, choices=STATUS_CHOICES, default='months', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Groups(models.Model):
    """Gruhlar yaratish uchun"""
    PENDING = 'Pending'
    ACTIVE = 'active'
    COMPLETED = 'completed'


    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACTIVE, 'Active'),
        (COMPLETED, 'Completed'),
    ]
    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(TeacherProfil, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='Pending', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course_id.name}-{self.name}: {self.teacher_id.user.get_full_name()}"


class Enrollments(models.Model):
    """Guruhga talaba royhatdan otish uchun"""
    ACTIVE = 'active'
    COMPLETED = 'completed'
    CANCELED = 'canceled'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (COMPLETED, 'Completed'),
        (CANCELED, 'Cancelled')
    ]

    student_id = models.ForeignKey(StudentProfil, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default=ACTIVE, blank=True, null=True)
    is_paid = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.id}.{self.student_id.user.username} - {self.group_id.name}"

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(fields=['student_id',], name='unique_student_group')
    #     ]
