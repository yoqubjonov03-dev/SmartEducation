from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users_app.views import TeacherProfilViewSet, StudentProfilViewSet, CoursesViewSet, GroupsViewSet, EnrollmentsViewSet


router = DefaultRouter()
router.register(r'TeacherProfil', TeacherProfilViewSet)
router.register(r'StudentProfil', StudentProfilViewSet)
router.register(r'Courses', CoursesViewSet)
router.register(r'Groups', GroupsViewSet)
router.register(r'Enrollment', EnrollmentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
