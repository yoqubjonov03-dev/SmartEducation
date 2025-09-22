from django_filters import rest_framework as django_filters
from users_app.models import Groups, Courses


class CoursesFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Courses
        fields = ['min_price', 'max_price']


class GroupsFilter(django_filters.FilterSet):
    course_name = django_filters.CharFilter(field_name='course_id__name', lookup_expr='icontains')

    class Meta:
        model = Groups
        fields = ['course_name', 'teacher_id', 'name', 'status']
