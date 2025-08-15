from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import StudentProfilViewset

router = DefaultRouter()
router.register(r'StudentProfil', StudentProfilViewset)

urlpatterns = [
    path('', include(router.urls)),
]
