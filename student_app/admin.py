from django.contrib import admin
from .models import StudentProfil
# Register your models here.
# admin.site.register(StudentProfil)
@admin.register(StudentProfil)
class StudentProfilAdmin(admin.ModelAdmin):
    list_display = ('user__first_name', 'birth_data', 'parent_name', 'parent_phone')
    search_fields = ('user__first_name', 'user__last_name', 'parent_name')

    # def get_last_name(self, obj):
    #     return obj.user.last_name
    #
    # get_last_name.short_description = 'Familiya'