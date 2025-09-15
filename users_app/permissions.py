from rest_framework import permissions

from users_app.models import TeacherProfil, StudentProfil, Groups, Enrollments


def is_teacher(user):
    """user Teacher ekanligini aniqlash True/False"""
    return TeacherProfil.objects.filter(user=user).exists()

def is_student(user):
    """user Student ekanligini aniqlash True/False"""
    return StudentProfil.objects.filter(user=user).exists()



class IsTeachersStudentsGroup(permissions.BasePermission):
    """Groups jadvali permission ni"""

    def has_permission(self, request, view):
        """Faqat login bo‘lgan foydalanuvchilar"""
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """is_superuser va is_staff ga mumkin"""
        if request.user.is_superuser or request.user.is_staff:
            return True
        """teacher faqat oz guruhini koradi"""
        # if is_teacher(request.user):
        if obj.teacher_id.user == request.user:
            return True
        """student oz gurihini koradi"""
        if Enrollments.objects.filter(student_id=request.user, group_id=obj).exists():
            return True


class IsAdminTeacherStudent(permissions.BasePermission):
    """TeacherProfil va StudentProfil uchun permission"""

    def has_permission(self, request, view):
        # Faqat login bo‘lgan foydalanuvchilar
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


    def has_object_permission(self, request, view, obj):

        """request.user hodim yoki admin bolsa ruhsad"""

        if request.user.is_superuser or request.user.is_staff:
            return True



        """student va teacher oz malumotini koroladi"""
        return obj.user_id == request.user.id


class IsTeacherStudentDaySchedules(permissions.BasePermission):
    """DaySchedule jadvali uchun permissions"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """Student va teacher oz guruhini jadvalini koroladi  """
        if request.user.is_superuser or request.user.is_staff:
            return
        teacher_group_ids = Groups.objects.filter(teacher_id__user_id=request.user.id).values_list('id', flat=True)
        student_group_ids = Enrollments.objects.filter(student_id_id=request.user.id).values_list('group_id_id',
                                                                                                  flat=True)

        if is_teacher(request.user):
            return obj.schedule_id.group_id_id in teacher_group_ids

        return obj.schedule_id.group_id_id in student_group_ids


class IsAdminIsStaff(permissions.BasePermission):
    """Admin va hodimga ruhsad berish"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_staff





