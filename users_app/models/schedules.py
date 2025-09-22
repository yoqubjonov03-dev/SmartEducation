from django.db import models
from .groups import Groups


class Schedules(models.Model):
    group_id = models.OneToOneField(Groups, on_delete=models.CASCADE)
    start_day = models.DateField()
    end_day = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.group_id.name}, {self.start_day}"




class DaySchedules(models.Model):
    EVERY_DAY='Every day'
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    STATUS_CHOICES = [
        (EVERY_DAY,'Every day'),
        (MONDAY, 'Monday'),
        (TUESDAY, 'Tuesday'),
        (WEDNESDAY, 'Wednesday'),
        (THURSDAY, 'Thursday'),
        (FRIDAY, 'Friday'),
        (SATURDAY, 'Saturday'),
        (SUNDAY, 'Sunday'),
    ]

    schedule_id = models.ForeignKey(Schedules, on_delete=models.CASCADE)
    week_day = models.CharField(max_length=12, choices=STATUS_CHOICES, default=EVERY_DAY)
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.schedule_id.group_id.name}, {self.week_day}"
