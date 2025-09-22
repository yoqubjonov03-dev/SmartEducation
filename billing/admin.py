from django.contrib import admin
from .models import Payments
# Register your models here.

@admin.register(Payments)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'enrollment_id__group_id__name', 'amount', 'payment_method',)
    search_fields = ('student_name', 'enrollment_id__group_id__name', 'payment_method')
    def student_name(self, obj):
        return obj.enrollment_id.student_id.user.get_full_name()
