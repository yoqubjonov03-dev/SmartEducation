from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users_app.models import StudentProfil, TeacherProfil
import unittest


# Create your tests here.
# python manage.py dumpdata products.Category --format=yaml --indent=4 > products/fixtures/categories.yaml

# @unittest.skip('vaqtincha ochirildi')
class TeacherProfilViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='adminroot')
        self.staff_user = User.objects.create_user(username='User2', password='adminroot', is_staff=True)
        self.user2 = User.objects.create_user(username='doi', password='adminroot')

        self.teacher1 = TeacherProfil.objects.create(
            user=self.user,
            specialty='python',
            experience_years=1,
            phone_number='932919894'
        )
        self.teacher2 = TeacherProfil.objects.create(
            user=self.staff_user,
            specialty='java',
            experience_years=3,
            phone_number='932365869'
        )

    def test_teacherprofil_list(self):
        url = reverse('teacherprofil-list')
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teacherprofil_filter_by_experience(self):
        url = reverse('teacherprofil-list') + f"?min_experience_years=2&max_experience_years=5"
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_teacherprofil_specialty(self):
        url = reverse('teacherprofil-list') + f'?specialty=python'
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_teacherprofil_create(self):
        url = reverse('teacherprofil-list')
        data = {
            'user': self.user2.id,
            'specialty': 'python',
            'experience_years': 1,
            'phone_number': '932919894'
        }
        self.client.force_authenticate(self.staff_user)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['specialty'], 'python')

    def test_teacherprofil_detail(self):
        url = reverse('teacherprofil-detail', args=[self.teacher1.id])
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['experience_years'], 1)

    def test_teacherprofil_delete(self):
        url = reverse('teacherprofil-detail', args=[self.teacher1.id])
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_permission_for_anonymuser_create(self):
        self.client.force_authenticate(user=None)
        url = reverse('teacherprofil-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class StudentProfilTestCase(APITestCase):
    fixtures = ['smarteducation_data.yaml']

    def setUp(self):
        self.staff_user = User.objects.get(id=1)
        self.student = StudentProfil.objects.get(id=1)

    def test_student_list(self):
        url = reverse('studentprofil-list')
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_student_create(self):
        url = reverse('studentprofil-list')
        self.client.force_authenticate(self.staff_user)
        data = {
            'user': self.staff_user.id,
            'parent_name': 'daoi',
            'parent_phone': '12547895',

        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_student_update(self):
        url = reverse('studentprofil-detail', args=[self.student.id])
        self.client.force_authenticate(self.staff_user)
        data = {
            'user': self.staff_user.id,
            'parent_name': 'Jon',
            'parent_phone': '12547895',
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['parent_name'], 'Jon')

    def test_student_delete(self):
        url = reverse('studentprofil-detail', args=[self.student.id])
        self.client.force_authenticate(self.staff_user)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_student_filter_parent_name(self):
        url = reverse('studentprofil-list') + f'?parent_name=' + self.student.parent_name
        self.client.force_authenticate(self.staff_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['parent_name'],"Dilshod o'g'li")
