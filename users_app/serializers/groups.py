from rest_framework import serializers
from users_app.models import Groups, Courses, Enrollments


class CoursesSerializer(serializers.ModelSerializer):
    groups_count = serializers.SerializerMethodField()

    class Meta:
        model = Courses
        fields = ['id', 'name', 'description', 'price', 'duration', 'groups_count']

    def get_groups_count(self, obj):
        return Groups.objects.filter(course_id=obj).count()


class GroupsSerializer(serializers.ModelSerializer):
    student_count = serializers.SerializerMethodField()
    teacher_name = serializers.SerializerMethodField()

    class Meta:
        model = Groups
        fields = ['id', 'name','course_id','teacher_id', 'status','start_date', 'end_date', 'teacher_name', 'student_count', 'start_date', 'end_date', ]

    def get_student_count(self, obj):
        return Enrollments.objects.filter(group_id=obj, status=Enrollments.ACTIVE).count()

    def get_teacher_name(self, obj):
        return obj.teacher_id.user.get_full_name()


class EnrollmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollments
        fields = ['id','student_id', 'group_id', 'enrollment_date', 'status','is_paid']

    # def validate(self, attrs):
    #     """bir user bita guruda birmarta boladi """
    #     student = attrs.get('student_id')
    #     group = attrs.get('group_id')
    #     if Enrollments.objects.filter(student_id=student, group_id=group).exists():
    #         raise serializers.ValidationError("Bu student allaqachon ushbu guruhga qo‘shilgan.")
    #     return attrs


