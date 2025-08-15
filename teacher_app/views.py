from django.shortcuts import render
from .models import TeacherProfil
from rest_framework import serializers, viewsets
# Create your views here.

class TeacherProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model=TeacherProfil
        fields = '__all__'
class TeacherProfilViewset(viewsets.ModelViewSet):
    queryset = TeacherProfil.objects.all()
    serializer_class = TeacherProfilSerializers
