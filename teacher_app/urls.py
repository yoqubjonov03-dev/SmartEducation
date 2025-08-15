from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import TeacherProfilViewset

router = DefaultRouter()
router.register(r'TeacherProfil', TeacherProfilViewset)


urlpatterns = [
    path('', include(router.urls)),
]
