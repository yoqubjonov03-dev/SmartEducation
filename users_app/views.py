from django.shortcuts import render
from .models import StudentProfil, TeacherProfil
from rest_framework import serializers, viewsets
# Create your views here.

class StudentProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model=StudentProfil
        fields = '__all__'

class StudentProfilViewset(viewsets.ModelViewSet):
    queryset = StudentProfil.objects.all()
    serializer_class = StudentProfilSerializers

class TeacherProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model=TeacherProfil
        fields = '__all__'

class TeacherProfilViewset(viewsets.ModelViewSet):
    queryset = TeacherProfil.objects.all()
    serializer_class = TeacherProfilSerializers

