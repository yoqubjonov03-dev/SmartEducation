from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User
from users_app.models import Schedules, DaySchedules, Groups, Courses, TeacherProfil
import unittest


# @unittest.skip('Vahtincha ochirildi')
class ScheduleTests(APITestCase):
    fixtures = ['smarteducation_data.yaml']

    def setUp(self):
        self.staff_user = User.objects.get(id=1)
        self.course = Courses.objects.get(id=1)
        self.teacher = TeacherProfil.objects.get(id=1)
        self.group1 = Groups.objects.get(id=1)
        self.group = Groups.objects.create(
            course_id=self.course,
            teacher_id=self.teacher,
            name='2P-25',
            start_date='2025-05-06',
            end_date='2025-06-08'
        )
        self.schedule = Schedules.objects.get(id=1)

    def test_schedule_list(self):
        url = reverse('schedules-list')
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_schedule_create(self):
        url = reverse('schedules-list')
        self.client.force_authenticate(self.staff_user)
        data = {
            'group_id': self.group.id,
            'start_day': '2025-10-25',
            'end_day': '2025-11-25'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_schetule_filter_group_name(self):
        url = reverse('schedules-list') + f'?group_name=' + self.group1.name
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_schedule_updete(self):
        url = reverse('schedules-detail', args=[self.schedule.id])
        self.client.force_authenticate(self.staff_user)
        data = {
            'group_id': self.group.id,
            'start_day': '2025-10-25',
            'end_day': '2025-11-25'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_schedule_delete(self):
        url = reverse('schedules-detail', args=[self.schedule.id])
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_schedule_permission_user(self):
        self.client.force_authenticate(user=None)
        url = reverse('schedules-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

# @unittest.skip('vaqtincha ishlamaydi')
class DayScheduleTests(APITestCase):
    fixtures = ['smarteducation_data.yaml']

    def setUp(self):
        self.staff_user = User.objects.get(id=1)
        self.dayschedule = DaySchedules.objects.get(id=1)
        self.schedule = Schedules.objects.get(id=1)
        self.group = Groups.objects.get(id=1)

    def test_dayschedule_list(self):
        url = reverse('dayschedules-list')
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 6)

    def test_dayschedule_filter_groupname(self):
        url = reverse('dayschedules-list') + f'?group_name=' + self.group.name
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 3)

    def test_dayschedule_filter_week_days(self):
        url = reverse('dayschedules-list') + f'?week_day=' + self.dayschedule.week_day
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dayschedule_filter_room(self):
        url = reverse('dayschedules-list') + f'?room=' + self.dayschedule.room
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_dayschedule_create(self):
        url = reverse('dayschedules-list')
        self.client.force_authenticate(self.staff_user)
        data = {
            'schedule_id': self.schedule.id,
            'week_day': 'Tuesday',
            'start_time': '10:20:00',
            'end_time': '12:20:00',
            'room': '3'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_dayschedule_updete(self):
        url = reverse('dayschedules-detail', args=[self.dayschedule.id])
        self.client.force_authenticate(self.staff_user)
        data = {
            'schedule_id': self.schedule.id,
            'week_day': 'Monday',
            'start_time': '10:20:00',
            'end_time': '12:20:00',
            'room': '2'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
