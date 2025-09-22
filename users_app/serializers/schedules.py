from rest_framework import serializers
from users_app.models import Schedules, DaySchedules


class SchedulesSerializer(serializers.ModelSerializer):
    group_name = serializers.SerializerMethodField()

    class Meta:
        model = Schedules
        fields = ['id', 'group_id', 'group_name', 'start_day', 'end_day', 'created_at', 'update_at']

    def get_group_name(self, obj):
        return obj.group_id.name


class DaySchedulesSerializer(serializers.ModelSerializer):
    group_name = serializers.SerializerMethodField()

    class Meta:
        model = DaySchedules
        fields = ['id', 'schedule_id', 'group_name', 'week_day', 'start_time', 'end_time', 'room']

    def get_group_name(self, obj):
        return obj.schedule_id.group_id.name



