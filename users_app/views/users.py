from django.shortcuts import render
from users_app.models import StudentProfil, TeacherProfil
from rest_framework import  viewsets
from users_app.serializers import TeacherProfilSerializers, StudentProfilSerializers
# Create your views here.



class StudentProfilViewSet(viewsets.ModelViewSet):
    queryset = StudentProfil.objects.all()
    serializer_class = StudentProfilSerializers



class TeacherProfilViewSet(viewsets.ModelViewSet):
    queryset = TeacherProfil.objects.all()
    serializer_class = TeacherProfilSerializers

