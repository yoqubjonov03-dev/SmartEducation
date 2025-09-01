from http.client import responses

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users_app.models import TeacherProfil
from django.contrib.auth.models import User

# Create your tests here.






class TeacherProfilTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='Admin1',
            email='admin15@gmail.com',
            password='root1')

        self.staff_user = User.objects.create_user(
            username='Admin2',
            email='admin25@gmail.com',
            password='root2',
            is_staff=True)


        self.teacher1 = TeacherProfil.objects.create(
            user=self.user,
            specialty="matematika",
            exprence_years='2',
            address='namangan viloyati',
            phone_number='932519894')

    def test_teacherprofil_list(self):
        url =reverse('teacherprofil-list')
        response =self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['user'],self.user.id)

    def test_teacherprofil_update(self):
        url =reverse('teacherprofil-detail',args=[self.teacher1.pk])
        data = { 'user':self.user.id,
            'specialty':"matematika",
            'exprence_years':'3',
            'address':'namangan viloyati',
            'phone_number':'932519894'}
        response =self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['exprence_years'], 3)

