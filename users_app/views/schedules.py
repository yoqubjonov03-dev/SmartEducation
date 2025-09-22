from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from users_app.models import DaySchedules, Schedules
from users_app.serializers import DaySchedulesSerializer, SchedulesSerializer

from django_filters import rest_framework as django_filters
from users_app.filters import SchedulesFilters, DaySchedulesFilter
from users_app.paginations import CustomPagination

from users_app.permissions import IsAdminIsStaff
from rest_framework.permissions import IsAuthenticated

class DaySchedulesViewSet(viewsets.ModelViewSet):
    queryset = DaySchedules.objects.all().order_by('id')
    serializer_class = DaySchedulesSerializer

    permission_classes = [IsAuthenticated, IsAdminIsStaff]
    pagination_class = CustomPagination
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_class = DaySchedulesFilter

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('group_name', openapi.IN_QUERY, description="Group name", type=openapi.TYPE_STRING),
        openapi.Parameter('week_days', openapi.IN_QUERY, description="Week Days ", type=openapi.TYPE_STRING),
        openapi.Parameter('start_time', openapi.IN_QUERY, description="Start Time ", type=openapi.TYPE_NUMBER),
        openapi.Parameter('room', openapi.IN_QUERY, description="Room", type=openapi.TYPE_STRING),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)





class SchedulesViewSet(viewsets.ModelViewSet):
    queryset = Schedules.objects.all().order_by('id')
    serializer_class = SchedulesSerializer

    permission_classes = [IsAuthenticated, IsAdminIsStaff]
    pagination_class = CustomPagination
    filter_backends = [django_filters.DjangoFilterBackend]
    filterset_class = SchedulesFilters

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('group_name', openapi.IN_QUERY, description="Group name", type=openapi.TYPE_STRING),

    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)