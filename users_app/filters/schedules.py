from random import choices

from django_filters import rest_framework as django_filters
from users_app.models import Schedules, DaySchedules


class DaySchedulesFilter(django_filters.FilterSet):
    STATUS_CHOICES = [
        ('monday', 'monday'),
        ('tuesday', 'tuesday'),
        ('wednesday', 'wednesday'),
        ('thursday', 'thursday'),
        ('friday', 'friday'),
        ('saturday', 'saturday'),
        ('sunday', 'sunday'),
    ]
    week_days = django_filters.ChoiceFilter(choices = STATUS_CHOICES)
    group_name = django_filters.CharFilter(field_name='schedule_id__group_id__name', lookup_expr='icontains')
    class Meta:
        model = DaySchedules
        fields = ['group_name','week_days','start_time','room']


class SchedulesFilters(django_filters.FilterSet):
    group_name = django_filters.CharFilter(field_name='group_id__name', lookup_expr='icontains')
    class Meta:
        model = Schedules
        fields = ['group_name']