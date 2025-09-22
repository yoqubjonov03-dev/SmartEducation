from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from django.contrib.auth.models import User

from users_app.models import Courses, Groups, Enrollments, TeacherProfil, StudentProfil
import unittest


# @unittest.skip('vaqtincha ochirildi')
class CoursesTests(APITestCase):
    fixtures = ['smarteducation_data.yaml']

    def setUp(self):
        self.staff_user = User.objects.get(id=1)
        self.user = User.objects.get(id=2)
        self.course = Courses.objects.get(id=1)

    def test_course_list(self):
        url = reverse('courses-list')
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_course_list_filter_by_price(self):
        url = reverse('courses-list') + f'?min_price=500000&max_price=800000'
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_course_create(self):
        url = reverse('courses-list')
        self.client.force_authenticate(self.staff_user)
        data = {
            'name': 'c++',
            'description': 'c++ asoslari',
            'price': 70000,

        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_course_updete(self):
        url = reverse('courses-detail', args=[self.course.id])
        self.client.force_authenticate(self.staff_user)
        data = {
            'name': 'C++',
            'description': 'C** backend',
            'price': 70000,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'C++')

    def test_course_list_permission(self):
        self.client.force_authenticate(user=None)
        url = reverse('courses-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_course_create_permission(self):
        self.client.force_authenticate(user=None)
        url = reverse('courses-list')
        data = {
            'name': 'C++',
            'description': 'C** backend',
            'price': 70000,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# @unittest.skip('Vaqtincha ochirish')
class GroupsTests(APITestCase):
    fixtures = ['smarteducation_data.yaml']

    def setUp(self):
        self.staff_user = User.objects.get(id=1)
        self.group = Groups.objects.get(id=1)
        self.course = Courses.objects.get(id=1)
        self.teacher = TeacherProfil.objects.get(id=1)

    def test_groups_list(self):
        url = reverse('groups-list')
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_group_filter_course_name(self):
        url = reverse('groups-list') + f'?course_name=' + self.course.name
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], '1P-25')

    def test_group_create(self):
        url = reverse('groups-list')
        data = {
            'course_id': self.course.id,
            'teacher_id': self.teacher.id,
            'name': '2P-25',
            'start_date': '2025-09-15',
            'end_date': '2025-12-15'
        }
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_group_updete(self):
        url = reverse('groups-detail', args=[self.group.id])
        data = {
            'course_id': self.course.id,
            'teacher_id': self.teacher.id,
            'name': '2P-25',
            'start_date': '2025-09-15',
            'end_date': '2025-12-15'
        }
        self.client.force_authenticate(self.staff_user)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_group_delete(self):
        url = reverse('groups-detail', args=[self.group.id])

        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_group_permission(self):
        self.client.force_authenticate(user=None)
        url = reverse('groups-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


# @unittest.skip('Vaqtincha ochirildi')
class EnrollmentsTests(APITestCase):
    fixtures = ['smarteducation_data.yaml']

    def setUp(self):
        self.staff_user = User.objects.get(id=1)
        self.group = Groups.objects.get(id=1)
        self.student = StudentProfil.objects.get(id=1)
        self.enrollment = Enrollments.objects.get(id=1)
        self.student2 = StudentProfil.objects.create(
            user=self.staff_user,
            parent_name='adad',
            parent_phone='652212555'

        )

    def test_enrollment_list(self):
        url = reverse('enrollments-list')
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 4)

    def test_enrollment_create(self):
        url = reverse('enrollments-list')
        self.client.force_authenticate(self.staff_user)
        data = {
            'group_id': self.group.id,
            'student_id': self.student2.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['group_id'], self.group.id)

    def test_enrollment_updete(self):
        url = reverse('enrollments-detail', args=[self.enrollment.id])
        self.client.force_authenticate(self.staff_user)
        data = data = {
            'group_id': self.group.id,
            'student_id': self.student2.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_enrollment_delete(self):
        url = reverse('enrollments-detail', args=[self.enrollment.id])
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_enrolment_permission_user(self):
        self.client.force_authenticate(user=None)
        url = reverse('enrollments-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
