from django.shortcuts import render
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from users_app.models import StudentProfil, TeacherProfil
from rest_framework import viewsets
from users_app.serializers import TeacherProfilSerializers, StudentProfilSerializers

from django_filters import rest_framework as django_filters
from users_app.paginations import CustomPagination
from rest_framework import filters
from users_app.filters import TeacherProfilFilter, StudentProfilFilters


# Create your views here.


class StudentProfilViewSet(viewsets.ModelViewSet):
    queryset = StudentProfil.objects.all()
    serializer_class = StudentProfilSerializers

    pagination_class = CustomPagination
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = StudentProfilFilters
    search_fields = ['user__last_name', 'user__first_name', 'address']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('age', openapi.IN_QUERY, description="age", type=openapi.TYPE_NUMBER),
        openapi.Parameter('min_age', openapi.IN_QUERY, description="min age ", type=openapi.TYPE_NUMBER),
        openapi.Parameter('max_age', openapi.IN_QUERY, description="max age", type=openapi.TYPE_NUMBER)
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TeacherProfilViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfil.objects.all()
    serializer_class = TeacherProfilSerializers

    pagination_class = CustomPagination
    filter_backends = [django_filters.DjangoFilterBackend, filters.SearchFilter]
    filterset_class = TeacherProfilFilter
    search_fields = ['user__last_name', 'user__first_name']

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('min_experience_years', openapi.IN_QUERY, description="min experience years ", type=openapi.TYPE_NUMBER),
        openapi.Parameter('max_experience_years', openapi.IN_QUERY, description="max experience years", type=openapi.TYPE_NUMBER)
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

