from rest_framework import serializers
from .models import Payments
from users_app.models import Enrollments


class PaymentsSerializer(serializers.ModelSerializer):
    group_name = serializers.SerializerMethodField()
    student_name = serializers.SerializerMethodField()

    class Meta:
        model = Payments
        fields = ['id', 'enrollment_id', 'group_name', 'student_name', 'stripe_charge_id', 'amount', 'payment_method']

    def get_group_name(self, obj):
        return obj.enrollment_id.group_id.name

    def get_student_name(self, obj):
        return obj.enrollment_id.student_id.user.get_full_name()

