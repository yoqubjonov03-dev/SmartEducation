from webbrowser import register

from django.contrib import admin
from .models import TeacherProfil, StudentProfil, Courses, Groups, Enrollments, DaySchedules, Schedules

# Register your models here.
# admin.site.register(TeacherProfil)
@admin.register(TeacherProfil)
class StudentProfilAdmin(admin.ModelAdmin):
    list_display = ('user__first_name', 'specialty', 'experience_years', 'phone_number')
    search_fields = ('user__first_name', 'user__last_name', 'parent_name')

@admin.register(StudentProfil)
class StudentProfilAdmin(admin.ModelAdmin):
    list_display = ('user__first_name', 'birth_date', 'parent_name', 'parent_phone')
    search_fields = ('user__first_name', 'user__last_name', 'parent_name')
admin.site.register(Courses)
admin.site.register(Groups)
admin.site.register(Enrollments)
admin.site.register(Schedules)
admin.site.register(DaySchedules)



