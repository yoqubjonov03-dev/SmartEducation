import django_filters
from rest_framework import serializers
from users_app.models import TeacherProfil, StudentProfil
from django.contrib.auth.models import User


class StudentProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model = StudentProfil
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Faqat TeacherProfil bo‘lmagan userlar chiqsin
        self.fields['user'].queryset = User.objects.exclude(studentprofil__isnull=False)


class TeacherProfilSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeacherProfil
        fields = '__all__'


