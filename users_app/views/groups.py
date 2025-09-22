from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from users_app.models import Courses, Groups, Enrollments
from users_app.serializers import CoursesSerializer, GroupsSerializer, EnrollmentsSerializer
from rest_framework import viewsets

from django_filters import rest_framework as django_filters
from users_app.filters import GroupsFilter, CoursesFilter
from rest_framework import filters
from users_app.paginations import CustomPagination

from users_app.permissions import IsTeachersStudentsGroup,IsAdminIsStaff
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer

    permission_classes = [ IsAdminIsStaff]
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = CoursesFilter
    search_fields = ['name', 'description']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('min_price', openapi.IN_QUERY, description="min price", type=openapi.TYPE_NUMBER),
        openapi.Parameter('max_price', openapi.IN_QUERY, description="max price ", type=openapi.TYPE_NUMBER),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all().order_by('id')
    serializer_class = GroupsSerializer
    permission_classes = [IsAuthenticated, IsTeachersStudentsGroup]

    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = GroupsFilter
    search_fields = ['name']
    pagination_class = CustomPagination

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('course_name', openapi.IN_QUERY, description="Course name", type=openapi.TYPE_STRING),
        openapi.Parameter('name', openapi.IN_QUERY, description="Groups name ", type=openapi.TYPE_STRING),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)



class EnrollmentsViewSet(viewsets.ModelViewSet):
    queryset = Enrollments.objects.all().order_by('id')
    serializer_class = EnrollmentsSerializer

    permission_classes = [IsAuthenticated, IsAdminUser]
    pagination_class = CustomPagination

