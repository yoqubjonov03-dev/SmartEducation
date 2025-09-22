from django_filters import rest_framework as django_filters
from users_app.models import StudentProfil, TeacherProfil
import datetime


class StudentProfilFilters(django_filters.FilterSet):


    class Meta:
        model = StudentProfil
        fields = ['parent_name']



class TeacherProfilFilter(django_filters.FilterSet):
    min_experience_years = django_filters.NumberFilter(field_name='experience_years', lookup_expr='gte')
    max_experience_years = django_filters.NumberFilter(field_name='experience_years', lookup_expr='lte')
    class Meta:
        model = TeacherProfil
        fields = ['specialty', 'min_experience_years', 'max_experience_years']