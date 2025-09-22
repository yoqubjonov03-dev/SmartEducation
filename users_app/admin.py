from webbrowser import register

from django.contrib import admin
from .models import TeacherProfil, StudentProfil, Courses, Groups, Enrollments, DaySchedules, Schedules


# Register your models here.
# admin.site.register(TeacherProfil)
@admin.register(TeacherProfil)
class TeacherProfilAdmin(admin.ModelAdmin):
    list_display = ('id','user__id','user__first_name', 'specialty', 'experience_years', 'phone_number')
    search_fields = ('user__first_name', 'user__last_name', 'parent_name')


@admin.register(StudentProfil)
class StudentProfilAdmin(admin.ModelAdmin):
    list_display = ('id','user__first_name', 'birth_date', 'parent_name', 'parent_phone')
    search_fields = ('user__first_name', 'user__last_name', 'parent_name')

@admin.register(Courses)
class CoursesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name', 'description')

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('id','name','course_id__name', 'full_name', 'status', 'start_date')
    search_fields = ('name', 'full_name')

    def full_name(self,obj):
        return obj.teacher_id.user.get_full_name()

@admin.register(Enrollments)
class EnrollmentsAdmin(admin.ModelAdmin):
    list_display = ('id','student_id__id','full_name', 'group_id__name', 'status','is_paid')
    search_fields = ('full_name', 'group_id__name')

    def full_name(self, obj):
        return obj.student_id.user.get_full_name()

@admin.register(Schedules)
class SchedulesAdmin(admin.ModelAdmin):
    list_display = ('group_id__name', 'start_day', 'end_day')
    search_fields = ('group_id__name',)

@admin.register(DaySchedules)
class DaySchedulesAdmin(admin.ModelAdmin):
    list_display = ('schedule_id__group_id__name', 'week_day', 'start_time', 'end_time')
    search_fields = ('schedule_id__group_id__name', 'week_day')
