from . import signals

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from billing.views import PaymentViewSet
from users_app import views




router = DefaultRouter()
router.register(r'Payments', PaymentViewSet)
router.register(r'TeacherProfil', views.TeacherProfilViewSet)
router.register(r'StudentProfil', views.StudentProfilViewSet)
router.register(r'Courses', views.CoursesViewSet)
router.register(r'Groups', views.GroupsViewSet)
router.register(r'Enrollments', views.EnrollmentsViewSet)
router.register(r'DaySchedules', views.DaySchedulesViewSet)
router.register(r'Schedules', views.SchedulesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
