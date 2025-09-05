from django_filters import rest_framework as django_filters
from users_app.models import StudentProfil, TeacherProfil
import datetime


class StudentProfilFilters(django_filters.FilterSet):
    age = django_filters.NumberFilter(method='filter_by_age')
    min_age = django_filters.NumberFilter(method='filter_by_min_age')
    max_age = django_filters.NumberFilter(method='filter_by_max_age')

    class Meta:
        model = StudentProfil
        fields = ['age', 'min_age', 'max_age']

    def filter_by_age(self, queryset, name, value):
        """Aniq yosh bo‘yicha filter."""

        today = datetime.date.today()
        start_date = today.replace(year=today.year - value - 1) + datetime.timedelta(days=1)
        end_date = today.replace(year=today.year - value)
        return queryset.filter(birth_date__range=(start_date, end_date))

    def filter_by_min_age(self, queryset, name, value):
        """Minimal yosh bo‘yicha filter."""

        today = datetime.date.today()
        max_birth_date = today.replace(year=today.year - value)
        return queryset.filter(birth_date__lte=max_birth_date)

    def filter_by_max_age(self, queryset, name, value):
        """Maksimal yosh bo‘yicha filter."""

        today = datetime.date.today()
        min_birth_date = today.replace(year=today.year - value - 1) + datetime.timedelta(days=1)
        return queryset.filter(birth_date__gte=min_birth_date)

class TeacherProfilFilter(django_filters.FilterSet):
    min_experience_years = django_filters.NumberFilter(field_name='experience_years', lookup_expr='gte')
    max_experience_years = django_filters.NumberFilter(field_name='experience_years', lookup_expr='lte')
    class Meta:
        model = TeacherProfil
        fields = ['specialty', 'min_experience_years', 'max_experience_years']