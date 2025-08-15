from django.shortcuts import render
from .models import StudentProfil
from rest_framework import serializers, viewsets
# Create your views here.

class StudentProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model=StudentProfil
        fields = '__all__'

class StudentProfilViewset(viewsets.ModelViewSet):
    queryset = StudentProfil.objects.all()
    serializer_class = StudentProfilSerializers