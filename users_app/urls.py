from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import TeacherProfilViewset, StudentProfilViewset

router = DefaultRouter()
router.register(r'TeacherProfil', TeacherProfilViewset)
router.register(r'StudentProfil', StudentProfilViewset)


urlpatterns = [
    path('', include(router.urls)),
]
