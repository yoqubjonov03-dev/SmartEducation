from rest_framework import serializers
from users_app.models import TeacherProfil, StudentProfil


class StudentProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model=StudentProfil
        fields = '__all__'


class TeacherProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model=TeacherProfil
        fields = '__all__'
